# -*- coding: utf-8 -*-

# Scrapy settings for pmscanner project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'pmscanner'

SPIDER_MODULES = ['pmscanner.spiders']
ITEM_PIPELINES = {
	'pmscanner.pipelines.StatusPipeline':500,
	'pmscanner.pipelines.BrandPipeline':600,
}
NEWSPIDER_MODULE = 'pmscanner.spiders'
FEED_URI = 'output.json'
FEED_FORMAT = 'jsonlines'
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'pmscanner (+http://www.yourdomain.com)'
