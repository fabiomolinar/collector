# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AliItem(scrapy.Item):
    #Primary fields
    results = scrapy.Field()
    walled_brands = scrapy.Field()
    currency = scrapy.Field()
    search_text = scrapy.Field()
    #calculated fields
    max_price = scrapy.Field()
    min_price = scrapy.Field()
    average = scrapy.Field()
    median = scrapy.Field()
    stddev = scrapy.Field()
    number_points = scrapy.Field()

    max_price_nc = scrapy.Field()
    min_price_nc = scrapy.Field()
    average_nc = scrapy.Field()
    median_nc = scrapy.Field()
    stddev_nc = scrapy.Field()
    number_points_nc = scrapy.Field()
    #Housekeeping fields
    used_url = scrapy.Field()
    project = scrapy.Field()
    spider = scrapy.Field()
    server_name = scrapy.Field()
    date_created = scrapy.Field()

class WatchItem(scrapy.Item):
    #Primary fields
    amount = scrapy.Field()
    currency = scrapy.Field()
    is_average = scrapy.Field()
    #Housekeeping fields
    used_url = scrapy.Field()
    project = scrapy.Field()
    spider = scrapy.Field()
    server_name = scrapy.Field()
    date_created = scrapy.Field()
