# -*- coding: utf-8 -*-

# Scrapy settings for pmscanner project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
import os
BOT_NAME = 'pmscanner'
PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
SPIDER_MODULES = ['pmscanner.spiders']
ITEM_PIPELINES = {
	'pmscanner.pipelines.StatusPipeline':500,
	'pmscanner.pipelines.BrandPipeline':600,
	'pmscanner.pipelines.ModelPipeline':400,
	'scrapy.contrib.pipeline.images.ImagesPipeline':1}

IMAGES_STORE = os.path.join(PROJECT_ROOT,"images")

IMAGES_MIN_HEIGHT = 100
IMAGES_MIN_WIDTH = 100
IMAGES_THUMBS = {
	'small':(100,100)
}
NEWSPIDER_MODULE = 'pmscanner.spiders'
FEED_URI = 'output.json'
FEED_FORMAT = 'jsonlines'
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'pmscanner (+http://www.yourdomain.com)'
