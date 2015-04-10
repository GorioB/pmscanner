import scrapy
import os
from scrapy.spider import Spider
from scrapy.http import Request
from scrapy.contrib.loader import ItemLoader
import re
from pmscanner.items import Guitar
from datetime import datetime,timedelta

class GuitarsSpider(Spider):
	name = 'guitars'
	allowed_domains = ['talk.philmusic.com']
	start_urls = [
		"http://talk.philmusic.com/index.php?board=167.0"
	]

	def __init__(self,brand='',model='',pages='',status='',*args,**kwargs):
		self.brand = brand
		self.model = model
		self.pages = pages
		self.status=status


		self.brandchoices=[]
		with open("brands.txt","r") as f:
			for line in f:
				self.brandchoices.append(line.strip())

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
		item = Guitar()
		item['link'] = re.sub(r'PHPSESSID=\w+',
			"",
			response.url)
		keyinfo = response.xpath('//div[@class="keyinfo"][1]')
		smalltext = keyinfo.xpath('div[@class="smalltext"]')
		date = smalltext.xpath('text()').extract()[-1].replace(u'\u00bb','').strip()
		if date.startswith("at"):
			day = smalltext.xpath('strong[2]/text()').extract()[0]
			if day=="Today":
				today = datetime.now()
			else:
				today = datetime.now()-timedelta(hours=24)
			at,time,am = date.split(" ")
			time = [int(i) for i in time.split(":")]
			if am=="PM":
				time[0]+=12
			today = today.replace(hour=time[0],
				minute=time[1],
				second=time[2])

			date = today.strftime("%B %d, %Y, %I:%M:%S %p")

		item['date_posted'] = date


		postbody = " ".join(response.xpath('//div[@class="post"][1]/div/text()').extract())
		posthead = keyinfo.xpath('h5/a/text()').extract()[0]
		post = posthead+postbody
		item['brand']="Unknown"
		for brand in self.brandchoices:
			if re.search(brand,post,re.IGNORECASE):
				item['brand']=brand


		if re.search("SOLD",post,re.IGNORECASE):
			item['status']="Sold"
		elif re.search("(FS|SALE)",post,re.IGNORECASE):
			item['status']="For Sale"
		elif re.search("(FT|TRADE)",post,re.IGNORECASE):
			item['status']="For Trade"
		else:
			item['status']='Unknown'

		yield item
