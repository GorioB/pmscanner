import scrapy
import os
from scrapy import signals
from scrapy.spider import Spider
from scrapy.http import Request
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import TakeFirst
from scrapy.xlib.pydispatch import dispatcher
import re
from pmscanner.items import Guitar
from datetime import datetime,timedelta
from generate_html import generate_html

class GuitarsSpider(Spider):
	name = 'guitars'
	allowed_domains = ['talk.philmusic.com']
	start_urls = [
		"http://talk.philmusic.com/index.php?board=167.0"
	]

	def __init__(self,brand='',model='',pages='',status='',*args,**kwargs):
		dispatcher.connect(self.quit,signals.spider_closed)
		self.brand = brand
		self.model = model
		self.pages = pages
		self.status = status

		if self.pages:
			for pagenumber in range(0,int(self.pages)*50,50)[1:]:
				self.start_urls.append(
					'http://talk.philmusic.com/index.php?board=167.%s' % str(pagenumber)
				)

	def parse(self,response):
		for url in response.xpath('//td[@class="subject windowbg2"]/div/span/a/@href').extract():
			yield(Request(
				url=url,
				callback=self.parse_item
				)
			)

	def parse_item(self,response):
		loader = ItemLoader(item=Guitar(),response=response)
		loader.add_value('link',re.sub(r'PHPSESSID=\w+',"",response.url))

		loader.add_xpath('date_posted',
			'//div[@class="keyinfo"][1]/div[@class="smalltext"]/strong[2]/text()')
		loader.add_xpath('date_posted',
			'//div[@class="keyinfo"][1]/div[@class="smalltext"]/text()')

		header_xpath = '//div[@class="keyinfo"][1]/h5/a/text()'
		body_xpath = '//div[@class="post"][1]/div/text()'

		loader.add_xpath('brand',
			header_xpath)
		loader.add_xpath('brand',
			body_xpath)

		loader.add_xpath('model',
			header_xpath)
		loader.add_xpath('model',
			body_xpath)

		loader.add_xpath('status',
			header_xpath)
		loader.add_xpath('status',
			body_xpath)

		# loader.add_xpath('contact',
		# 	header_xpath,
		# 	re=r'(0|63)[0-9]{10}')
		loader.add_xpath('contact',
			body_xpath,
			re=r'[63|0][0-9]{10}')

		loader.add_xpath('price',
			body_xpath,
			re=r'[0-9]*\.?[0-9][k|K]')

		loader.add_xpath('image_urls',
			'//div[@class="post"][1]/div/img/@src')

		yield loader.load_item()

	def quit(self,spider):
		generate_html()