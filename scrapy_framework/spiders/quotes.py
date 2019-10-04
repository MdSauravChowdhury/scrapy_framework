# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.request import Request

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
    	quotes = response.xpath('//*[@class="quote"]')

    	for quote in quotes:

	    	title = response.xpath("//*[@class='text']/text()").extract_first()
	    	writer = response.xpath("//*[@class='author']/text()").extract_first()
	    	meta_tag = response.xpath('.//*[@itemprop="keywords"]/@content').extract_first()

	    	yield {'THAT OUR QUOTES': title, 'Author':writer, 'Tag':meta_tag}

        	
	    # next_page_url = response.xpath("//*[@class='next']/a/@href").extract_first()
	    # absoulate_url = response.urljoin(next_page_url)

	    # yield scrapy.Request(absoulate_url)


            # next_page_url = quote.xpath('//*[@class="next"]/a/@href').extract_first()
            # absoult_url   = response.urljoin(next_page_url)
            
            # yield scrapy.Request(absoult_url)