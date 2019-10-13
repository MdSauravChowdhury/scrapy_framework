# -*- coding: utf-8 -*-
import scrapy


class YellowCrawlSpider(scrapy.Spider):
    name = 'yellow_crawl'
    allowed_domains = ['yellowpages.com']
    start_urls = [
        'https://www.yellowpages.com/new-york-ny/business-insurance',
        'https://www.yellowpages.com/new-york-ny/business-insurance?page=2',
        'https://www.yellowpages.com/new-york-ny/business-insurance?page=3',
        ]

    def parse(self, response):
        target = response.xpath('.//*[@class="info"]')

        for item in target:
            access_dir = item.xpath('.//*[@class="business-name"]/@href').extract_first()
            access_item= response.urljoin(access_dir)

            yield scrapy.Request(access_item, callback=self.parse_item)
    
    def parse_item(self, response):
        bus_name= response.xpath(".//*[@class='sales-info']/h1/text()").extract_first()
        address = response.xpath(".//*[@class='address']/text()").extract_first()
        phone_nu= response.xpath(".//*[@class='phone']/text()").extract_first()
        website = response.xpath(".//*[@class='business-card-footer']/a/@href").extract_first()
        email = response.xpath('.//*[@class="email-business"]/@href').extract_first()

        # Addtional informations
        general_info = response.xpath(".//*[@class='general-info']/p/text()").extract_first()
        #ext_phone_fax= response.xpath(".//*[@class='extra-phones']/p/span/text()").extract()[1]
        brand = response.xpath(".//*[@class='brands']/p/text()").extract_first()
        neighborhood = response.xpath(".//*[@class='neighborhoods']/span/a/text()").extract()
        other_link = response.xpath(".//*[@class='other-links']/@href").extract_first()
        language = response.xpath(".//*[@class='languages']/text()").extract_first()
        category = response.xpath(".//*[@class='categories']/span/a/text()").extract()

        # dict_item = []
        # if bus_name and address and phone_nu and \
        #      website and email and general_info and brand \
        #          and neighborhood and other_link and \
        #          language and category:
        #     dict_item+=[dict_item]

        yield {
            'Business Name': bus_name,
            'Business Address': address,
            'Primary Phone': phone_nu,
            'Website': website,
            'Email': email,
            'General Info': general_info,
            #'Phone And Fax': ext_phone_fax,
            'Brand': brand,
            'Neighborhoods': neighborhood,
            'Website Extra': other_link,
            'Language': language,
            'Category': category,
        }