# -*- coding: utf-8 -*-

BOT_NAME = 'adidas-product_crawler'

SPIDER_MODULES = ['adidas-product_crawler.spiders']
NEWSPIDER_MODULE = 'adidas-product_crawler.spiders'



USER_AGENT = 'Mozilla/5.0'


ROBOTSTXT_OBEY = True


FEED_FORMAT = "csv"
FEED_URI = "tmp/%(name)s.csv"


LOG_ENABLED=False


DEPTH_LIMIT=2
FEED_EXPORT_FIELDS=["product_name", "price", "source", "product_url","image_url"]
