import re
import json
from urlparse import urlparse


from scrapy.selector import Selector
try:
    from scrapy.spider import Spider
except:
    from scrapy.spider import BaseSpider as Spider
from scrapy.utils.response import get_base_url
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.selector import HtmlXPathSelector
from database.items import databaseItem

from scrapy.log import *

class CommonSpider(CrawlSpider):
	name = 'brands.py'
	allowed_domains = ['usedprice.com']
	start_urls = ['http://www.usedprice.com/items/guitars-musical-instruments/index.html']

	rules = (
 
		Rule(LinkExtractor(allow=( )), callback='parse_item'),
    )


	def parse_item(self, response):
		hxs = HtmlXPathSelector(response)
    		item = databaseItem()
    		datao = datao = hxs.xpath('//tr[@class="oddItemColor baseText"]')
		datae = datae = hxs.xpath('//tr[@class="evenItemColor baseText"]')
    		tmpNextPage = hxs.xpath('//div[@class="baseText blue"]/span[@id="pnLink"]/a/@href').extract()
    		for attr in datao:
			modelInfo = attr.xpath('.//b/text()').extract()
			instrInfo = attr.xpathxpath('.//td//text()').extract()
			item['modelInfo'].append = modelInfo
			item['instrInfo'].append = instrInfo
			return databaseItem(modelInfo = modelInfo[1:], instrInfo = instrInfo[2:])
		for attr in datae:
			modelInfo = attr.xpath('.//b/text()').extract()
			instrInfo = attr.xpathxpath('.//td//text()').extract()
			item['modelInfo'].append = modelInfo
			item['instrInfo'].append = instrInfo
			return databaseItem(modelInfo = modelInfo[1:], instrInfo = instrInfo[2:])
					
			

