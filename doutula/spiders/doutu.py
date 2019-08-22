# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from scrapy_redis.spiders import RedisCrawlSpider
from ..items import DoutulaItem

scrapy.Selector
class DoutuSpider(RedisCrawlSpider):
    name = 'doutu'
    allowed_domains = ['www.doutula.com']
    # start_urls = ['http://www.doutula.com/photo/list/?page=0']
    redis_key = "DoutuSpider:start_urls"

    # 动态域的获取
    # def __init__(self, *args, **kwargs):
    #     # Dynamically define the allowed domains list.
    #     domain = kwargs.pop('domain', '')
    #     self.allowed_domains = filter(None, domain.split(','))
    #     super(DoutuSpider, self).__init__(*args, **kwargs)
    rules = [
        Rule(LinkExtractor(allow=r'page=\d+'), callback='parse_item', follow=True)
    ]

    def parse_item(self, response):
        for i in response.xpath('//a[@class="col-xs-6 col-sm-3"]'):
            item = DoutulaItem()
            item['name'] = i.xpath('.//p/text()').extract()[0]
            item['link'] = i.xpath('.//img/@data-original').extract()[0]
            yield item
