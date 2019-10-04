# -*- coding: utf-8 -*-
import scrapy


class TopQuoteSpider(scrapy.Spider):
    name = 'top_quote'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        #Box content
        quotes = response.xpath(".//*[@class='quote']")
        for quote in quotes:
            content = quote.xpath(".//*[@class='text']/text()").extract_first()
            author  = quote.xpath(".//*[@class='author']/text()").extract_first()
            topic   = quote.xpath(".//*[@class='keywords']/@content").extract_first()

            yield {
                'QUOTES':content,
                'Author':author,
                'Tags': topic
            }

        next_page_url = response.xpath(".//*[@class='next']/a/@href").extract_first()
        absoulate_next_page = response.urljoin(next_page_url)

        yield scrapy.Request(absoulate_next_page)