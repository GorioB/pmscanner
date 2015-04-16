# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem

class PmscannerPipeline(object):
    def process_item(self, item, spider):
        return item

class FilterPipeline(object):
	def __init__(self):
		self.field = ""

	def process_item(self,item,spider):
		if spider.__dict__[self.field]:
			print item[self.field],spider.__dict__[self.field]
			if spider.__dict__[self.field] not in item[self.field]:
				raise DropItem("Incorrect %s in %s." % (self.field,item))
		return item

class StatusPipeline(FilterPipeline):
	def __init__(self):
		self.field="status"

class BrandPipeline(FilterPipeline):
	def __init__(self):
		self.field="brand"

class ModelPipeline(FilterPipeline):
	def __init__(self):
		self.field="model"