# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import traceback
import logging

import dj_database_url
import psycopg2

from twisted.internet import defer
from twisted.enterprise import adbapi
from scrapy.exceptions import NotConfigured
from scrapy.exceptions import DropItem

class AliPipeline(object):
    """Pipeline to write results to DB"""

    @classmethod
    def from_crawler(cls, crawler):
        # Get PostgreSQL URL from settings
        postgresql_url = (
            "postgresql://" +
            crawler.settings.get('DB_USER', "") + ":" +
            crawler.settings.get('DB_PASS', "") + "@" +
            crawler.settings.get('DB_HOST', "") + ":" +
            crawler.settings.get('DB_PORT', "") + "/" +
            crawler.settings.get('DB_NAME', "")
        )

        # If doesn't exist, disable the pipeline
        if not postgresql_url:
            raise NotConfigured

        # Create the class
        return cls(postgresql_url)
    
    def __init__(self, postgresql_url):
        """Opens a PostgreSQL connection pool"""
        # Store the url for future reference
        self.postgresql_url = postgresql_url
        # Report connection error only once
        self.report_connection_error = True

        # Parse PostgreSQL URL and try to initialize a connection
        conn_kwargs = AliPipeline.parse_postgresql_url(postgresql_url)
        self.dbpool = adbapi.ConnectionPool('psycopg2',
                                            **conn_kwargs)

    def close_spider(self, spider):
        """Discard the database pool on spider close"""
        self.dbpool.close()

    @defer.inlineCallbacks
    def process_item(self, item, spider):
        """Processes the item. Does insert into PostgreSQL"""
        
        logger = spider.logger

        # If there is no item, that's probably because there were no results returned at all
        if len(item) <= 0:
            raise DropItem("No items on the pipeline")

        try:
            yield self.dbpool.runInteraction(self.do_replace, item)
        except psycopg2.OperationalError:
            if self.report_connection_error:
                logger.error("Can't connect to PostgreSQL: %s" % self.postgresql_url)
                self.report_connection_error = False
            print(traceback.format_exc())
            

        # Return the item for the next stage
        defer.returnValue(item)
    @staticmethod
    def do_replace(tx, item):
        """Does the actual INSERT"""

        sql = """INSERT INTO ali_search (
            search_text, results, walled_brands, currency, 
            max_price, min_price, average, median, stddev, number_points, 
            max_price_nc, min_price_nc, average_nc, median_nc, stddev_nc, number_points_nc, 
            used_url, project, spider, server_name, date_created)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

        args = (
            item["search_text"][0],
            item.get("results",[0])[0],
            item.get('walled_brands',[]),
            item["currency"][0],
            item["max_price"][0],
            item["min_price"][0],
            item["average"][0],
            item["median"][0],
            item["stddev"][0],
            item["number_points"][0],
            item["max_price_nc"][0],
            item["min_price_nc"][0],
            item["average_nc"][0],
            item["median_nc"][0],
            item["stddev_nc"][0],
            item["number_points_nc"][0],
            item["used_url"][0],
            item["project"][0],
            item["spider"][0],
            item["server_name"][0],
            item["date_created"][0]
        )

        tx.execute(sql, args)

    @staticmethod
    def parse_postgresql_url(postgresql_url):
        """
        Parses url and prepares arguments for
        adbapi.ConnectionPool()
        """

        params = dj_database_url.parse(postgresql_url)

        conn_kwargs = {}
        conn_kwargs['host'] = params['HOST']
        conn_kwargs['user'] = params['USER']
        conn_kwargs['password'] = params['PASSWORD']
        conn_kwargs['dbname'] = params['NAME']
        conn_kwargs['port'] = params['PORT']

        # Remove items with empty values
        conn_kwargs = dict((k, v) for k, v in conn_kwargs.items() if v)

        return conn_kwargs

