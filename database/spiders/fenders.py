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


from .log import *

class CommonSpider(CrawlSpider):
    name = 'fender'
    allowed_domains = ['usedprice.com']
    start_urls = ['http://www.usedprice.com/items/guitars-musical-instruments/fender/?ob=model_asc#results']

    rules = (
 
        Rule(LinkExtractor(allow=( )), callback='parse_item'),


    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        item = []
        data = hxs.select('//td[@class="itemResult"]')
        tmpNextPage = hxs.select('//div[@class="baseText blue"]/span[@id="pnLink"]/a/@href').extract()
        for attr in data:
		item = RowItem()
		instrInfo = attr.select('//tr[@class="oddItemColor baseText"]/span[@class="itemResult"]').extract()
		item['attr'] = instrInfo
		print "Instrument Info: ", instrInfo
		yield item
	
	for NextPageLink in tmpNextPage
		m = re.search("Location," NextPageLink
		if m:	
			NextPage = NextPageLink
			print "Next Page: ", NextPage 
			yield Request("http://usedprice.com/"+NextPage, callback= self.parse)
		else: 
			NextPage = 'None'

