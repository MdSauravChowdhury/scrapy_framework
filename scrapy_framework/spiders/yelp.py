# -*- coding: utf-8 -*-
import scrapy


class YelpSpider(scrapy.Spider):
    name = 'yelp'
    allowed_domains = ['yelp.com']
    start_urls = ['https://www.yelp.com/search?find_desc=Coffee+%26+Tea&find_loc=San+Francisco%2C+CA&ns=1']

    def parse(self, response):
        selector = response.xpath('.//p/a/@href').extract()

        for access_link in selector:
            next_page = response.urljoin(access_link)

            yield scrapy.Request(next_page, callback=self.parse_item)


    def parse_item(self, response):
        title = response.xpath(".//h1/text()").extract_first()

        yield {
            'Title':title
        }