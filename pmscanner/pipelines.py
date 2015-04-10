# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem

class PmscannerPipeline(object):
    def process_item(self, item, spider):
        return item

class StatusPipeline(object):
	def process_item(self,item,spider):
		if spider.status:
			if item['status'] not in (spider.status,"Unknown"):
				raise DropItem("Incorrect status in %s" % item)
			else:
				return item
		else:
			return item