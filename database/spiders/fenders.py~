import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.lxmlhtml.LxmlLinkExtractor import LxmlLinkExtractor

class MySpider(CrawlSpider):
    name = 'usedprice.com'
    allowed_domains = ['usedprice.com']
    start_urls = ['http://www.usedprice.com/items/guitars-musical-instruments/fender/?ob=model_asc#results']

    rules = (
        # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
        Rule(LxmlLinkExtractor(allow=('items/guitars-musical-instruments/fender/electric-guitar/?ob=model_asc&pn=', )), callback='parse_item'),

        # Extract links matching 'item.php' and parse them with the spider's method parse_item
       # Rule(LinkExtractor(allow=('item\.php', )), callback='parse_item'),
    )

    def parse_item(self, response):
        self.log('Hi, this is an item page! %s' % response.url)
        item = scrapy.Item()
       # item['id'] = response.xpath('//td[@class="itemResult"]/text()').re(r'ID: (\d+)')
        item['name'] = response.xpath('//td[@class="itemResult"]/text()').extract()
      #  item['description'] = response.xpath('//td[@id="item_description"]/text()').extract()
        return item
