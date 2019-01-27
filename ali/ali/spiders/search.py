# -*- coding: utf-8 -*-
import scrapy
import datetime
import socket
import logging
import re
import numpy

from functools import reduce

from scrapy import Selector
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose
from scrapy.exceptions import CloseSpider
from ali.items import AliItem

class SearchSpider(scrapy.Spider):
    name = 'search'
    allowed_domains = ['aliexpress.com']
    custom_settings = {
        "ALLOW_ALIPIPELINE": True
    }

    def start_requests(self):
        query_param = {
            'catId': '0',
            'initiative_id': 'SB_' + datetime.datetime.today().strftime('%Y%m%d%H%M%S'),
            'SearchText': 'fidget spinner',
            'g':'n'
        }
        #gets search text from command line through the -a argument
        search_text = getattr(self, 'searchtext', None)
        if search_text is not None:
            query_param["SearchText"] = search_text
        start_url = "".join(['https://www.aliexpress.com/wholesale?catId=',
            query_param["catId"],
            '&initiative_id=',
            query_param["initiative_id"],
            '&SearchText=',
            query_param["SearchText"],
            '&g=',
            query_param["g"]])
        yield scrapy.Request(start_url, meta={'search_text':search_text})

    def parse(self, response):
        # --- Getting price data ---
        first_items = response.xpath('//ul[contains(@id,"hs-list-items")]//span[@itemprop="price"]/text()').extract()
        # --- If first items length is zero, no results have returned and we should drop ---
        if len(first_items) <= 0:
            raise CloseSpider('No results returned')
        below_first_items_text = response.xpath('//div[contains(@id,"below-list-items")]/script/text()').extract_first()
        below_first_items = Selector(text=below_first_items_text).xpath('//span[@itemprop="price"]/text()').extract()
        items = first_items + below_first_items
        
        for i,item in enumerate(items):
            if "-" in item:
                item = "".join(re.findall('[0-9.-]',item)).rstrip(".")
                item = item.split("-")
                item = [float(number) for number in item]
                items[i] = reduce(lambda x,y : x+y , item)/len(item)
            else:
                items[i] = float("".join(re.findall('[0-9.-]',item)).rstrip("."))
        
        #Filtering the data
        items_nc = numpy.array(items)
        d = numpy.abs(items_nc - numpy.median(items_nc))
        mdev = numpy.median(d)
        s = d/mdev if mdev else 0.0
        threshold = 3
        items_c = items_nc[s<threshold]

        #Getting currency data
        cookies = response.headers.getlist('Set-Cookie')        
        for cookie in cookies:
            if b"c_tp=" in cookie:
                currency = cookie.split(b"c_tp=")[-1].split(b";")[0].decode("utf-8")
        
        # --- Assigning items ---
        l = ItemLoader(item=AliItem(), response=response)
        #Primary items
        l.add_value('search_text',response.meta['search_text'])
        l.add_xpath('results', '//strong[@class="search-count"][1]/text()', MapCompose(lambda i : i.replace(",",""), int))
        l.add_xpath('walled_brands', '//div[@id="brands-wall-content"]/ul/li/a/@title')
        l.add_value('currency',currency)

        #calculated items
        l.add_value('max_price',numpy.amax(items_c))
        l.add_value('min_price',numpy.amin(items_c))
        l.add_value('average',numpy.mean(items_c))
        l.add_value('median',numpy.median(items_c))
        l.add_value('stddev',numpy.std(items_c))
        l.add_value('number_points',len(items_c))
        
        l.add_value('max_price_nc',numpy.amax(items_nc))
        l.add_value('min_price_nc',numpy.amin(items_nc))
        l.add_value('average_nc',numpy.mean(items_nc))
        l.add_value('median_nc',numpy.median(items_nc))
        l.add_value('stddev_nc',numpy.std(items_nc))
        l.add_value('number_points_nc',len(items_nc))
         
        #Housekeeping items
        l.add_value('used_url', response.url)
        l.add_value('project', self.settings.get('BOT_NAME'))
        l.add_value('spider', self.name)
        l.add_value('server_name', socket.gethostname())
        l.add_value('date_created', datetime.datetime.now())
        return l.load_item()