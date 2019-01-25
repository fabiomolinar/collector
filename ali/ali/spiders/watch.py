# -*- coding: utf-8 -*-
import scrapy
import datetime
import socket

from scrapy.spiders import CrawlSpider
from scrapy.loader import ItemLoader
from scrapy.exceptions import CloseSpider

from ali.items import WatchItem
from ali.utils.reader import PriceReader


class WatchSpider(CrawlSpider):
    name = 'watch'
    allowed_domains = ['aliexpress.com']
    
    def start_requests(self):
        link_text = getattr(self, 'link', None)
        link = eval(link_text)
        meta = {
            "data_path": getattr(self, 'data', None),
            "currency_path": getattr(self, 'currency', None),
            "amount_path": getattr(self, 'amount', None),
            "preffered_currency": getattr(self, 'preffered_currency', None),
        }
        yield scrapy.Request(link, meta=meta)

    def parse_item(self, response):
        pr = PriceReader(response.meta["preffered_currency"])
        data_string = response.xpath(response.meta["data_path"]).extract_first
        currency_string = response.xpath(response.meta["currency_path"]).extract_first()
        amount_string = response.xpath(response.meta["amount_path"]).extract_first()
        if not pr.read(data_string, currency=currency_string, amount=amount_string):
            raise CloseSpider("Couldn't parse amount and currency")

        l = ItemLoader(item=WatchItem(), response=response)
        #Input items
        l.add_value('data_path', response.meta["data_path"])
        l.add_value('currency_path', response.meta["currency_path"])
        l.add_value('amount_path', response.meta["amount_path"])
        #Primary items
        l.add_value('amount', pr.amount)
        l.add_value('currency', pr.currency)
        #Housekeeping items
        l.add_value('used_url', response.url)
        l.add_value('project', self.settings.get('BOT_NAME'))
        l.add_value('spider', self.name)
        l.add_value('server_name', socket.gethostname())
        l.add_value('date_created', datetime.datetime.now())

        return l.load_item()
