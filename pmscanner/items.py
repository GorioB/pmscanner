# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PmscannerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class Guitar(scrapy.Item):
	brand = scrapy.Field()
	model = scrapy.Field()
	price = scrapy.Field()
	contact = scrapy.Field()
	link = scrapy.Field()
	date_posted = scrapy.Field()