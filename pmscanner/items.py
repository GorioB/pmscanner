# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import TakeFirst,Join
from pmscanner.processors import GetDate,GetBrand,GetStatus

class Guitar(scrapy.Item):
	brand = scrapy.Field(output_processor=GetBrand("brands.txt"))
	model = scrapy.Field()
	price = scrapy.Field()
	contact = scrapy.Field()
	link = scrapy.Field(output_processor=TakeFirst())
	date_posted = scrapy.Field(output_processor=GetDate())
	status = scrapy.Field(output_processor=GetStatus())