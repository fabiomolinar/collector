# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
watcher_domains = [
    'aliexpress.com'
]

watcher_mapping = [
    {
        "domain": "aliexpress.com",
        "currency": [
            '//div[contains(@class, "p-price-content")]//span[contains(@itemprop, "priceCurrency")]/@content'
        ],
        "amount": [
            '//div[contains(@class, "p-price-content")]//span[contains(@itemprop, "lowPrice")]/text()',
            '//div[contains(@class, "p-price-content")]//span[contains(@class, "p-price")]/text()',
            '//div[contains(@class, "p-price-content")]//span[contains(@itemprop, "highPrice")]/text()',
            
        ]
    }
]