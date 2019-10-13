# -*- coding: utf-8 -*-
import scrapy


class BdnewsSpider(scrapy.Spider):
    name = 'bdnews'
    allowed_domains = ['bdnews24.com']
    start_urls = ['http://bdnews24.com/']

    def parse(self, response):
        pass
