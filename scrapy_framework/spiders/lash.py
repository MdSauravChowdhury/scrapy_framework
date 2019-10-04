# -*- coding: utf-8 -*-
import scrapy


class LashSpider(scrapy.Spider):
    name = 'lash'
    allowed_domains = ['yellowpages.com']
    start_urls = [
        'https://www.yellowpages.com/search?search_terms=real+estate&geo_location_terms=Los+Angeles%2C+CA',
        'https://www.yellowpages.com/search?search_terms=real%20estate&geo_location_terms=Los%20Angeles%2C%20CA&page=2',
        'https://www.yellowpages.com/search?search_terms=real%20estate&geo_location_terms=Los%20Angeles%2C%20CA&page=3',
        'https://www.yellowpages.com/search?search_terms=real%20estate&geo_location_terms=Los%20Angeles%2C%20CA&page=4',
        'https://www.yellowpages.com/search?search_terms=real%20estate&geo_location_terms=Los%20Angeles%2C%20CA&page=5',
        'https://www.yellowpages.com/search?search_terms=real%20estate&geo_location_terms=Los%20Angeles%2C%20CA&page=6',
        'https://www.yellowpages.com/search?search_terms=real%20estate&geo_location_terms=Los%20Angeles%2C%20CA&page=7',
        'https://www.yellowpages.com/search?search_terms=real%20estate&geo_location_terms=Los%20Angeles%2C%20CA&page=8',
        'https://www.yellowpages.com/search?search_terms=real%20estate&geo_location_terms=Los%20Angeles%2C%20CA&page=9',
        'https://www.yellowpages.com/search?search_terms=real%20estate&geo_location_terms=Los%20Angeles%2C%20CA&page=10',
        'https://www.yellowpages.com/search?search_terms=real%20estate&geo_location_terms=Los%20Angeles%2C%20CA&page=11',
        'https://www.yellowpages.com/search?search_terms=real%20estate&geo_location_terms=Los%20Angeles%2C%20CA&page=12',
        'https://www.yellowpages.com/search?search_terms=real%20estate&geo_location_terms=Los%20Angeles%2C%20CA&page=13',
        'https://www.yellowpages.com/search?search_terms=real%20estate&geo_location_terms=Los%20Angeles%2C%20CA&page=14',
        ]

    def parse(self, response):
        sel = response.xpath(".//*[@class='info']")

        for item in sel:
            name     = item.xpath(".//*[@class='business-name']/span/text()").extract_first()
            tel_num  = item.css("div.phones::text").extract_first()
            address  = item.xpath(".//*[@class='street-address']/text()").extract_first()
            location = item.xpath(".//*[@class='locality']/text()").extract_first()

            if name and tel_num and address and location:
                
                yield {
                    'NAME':name,
                    'TELEPHONE':tel_num,
                    'Address':address,
                    'Location':location
                }
