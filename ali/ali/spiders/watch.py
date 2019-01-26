# -*- coding: utf-8 -*-
import scrapy
import datetime
import socket
import ast

from scrapy.spiders import CrawlSpider
from scrapy.loader import ItemLoader
from scrapy.exceptions import CloseSpider

from ali.items import WatchItem
from ali.utils.reader import PriceReader


class WatchSpider(CrawlSpider):
    name = 'watch'
    from ali.spiders import watcher_domains as allowed_domains
    
    def start_requests(self):
        link = getattr(self, 'link', "None")
        meta = {
            "data_path": ast.literal_eval(getattr(self, 'data', "None")),
            "currency_path": ast.literal_eval(getattr(self, 'currency', "None")),
            "amount_path": ast.literal_eval(getattr(self, 'amount', "None")),
            "preffered_currency": ast.literal_eval(getattr(self, 'preffered_currency', "None")),
        }
        yield scrapy.Request(link, meta=meta)
    
    def parse_item(self, response):
        pr = PriceReader(response.meta["preffered_currency"])
        data_string = self.__class__.retrieve_strings(response, response.meta["data_path"])
        currency_string = self.__class__.retrieve_strings(response, response.meta["currency_path"])
        amount_string = self.__class__.retrieve_strings(response, response.meta["amount_path"])
        if not pr.read(data_string, currency=currency_string, amount=amount_string):
            raise CloseSpider("Couldn't parse amount and currency")

        l = ItemLoader(item=WatchItem(), response=response)
        #Input items
        l.add_value('data_string', response.meta["data_string"])
        l.add_value('currency_string', response.meta["currency_string"])
        l.add_value('amount_string', response.meta["amount_string"])
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

    @classmethod
    def retrieve_strings(cls, response, items):
        if type(items) != list:
            items = [items]
        result = ""
        for i in items:
            extracted = response.xpath(i).extract_first()
            if type(extracted) == str:
                result += extracted
        return result if result != "" else None