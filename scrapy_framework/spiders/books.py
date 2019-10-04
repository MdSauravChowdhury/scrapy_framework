# -*- coding: utf-8 -*-
import scrapy

# this is our dynamiac funcations callback by product value data
def product_info(response, value):
    return response.xpath('//th[text()=" '+ value +' "]/following-sibling::td/text()').extract_first()
   # return response.xpath('//th[text()=" '+ value +' "]/following-sibling::td/text()').extract_first()

class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        singel_pro = response.xpath('.//h3/a/@href').extract()

        for product in singel_pro:
            join_pro = response.urljoin(product)

            yield scrapy.Request(join_pro, callback=self.parse_item)

        #  NEXT PAGE URL JOIN
        next_page_url = response.xpath('.//*[@class="next"]/a/@href').extract_first()
        absoulate_next_page = response.urljoin(next_page_url)

        yield scrapy.Request(absoulate_next_page)

    
    def parse_item(self, response):
        product_name  = response.xpath(".//h1/text()").extract_first()
        product_price = response.xpath(".//*[@class='price_color']/text()").extract_first()
        product_rating= response.xpath('.//*[contains(@class, "star-rating")]/@class').extract_first()
        product_rating= product_rating.replace('star-rating', "")
        product_desc  = response.xpath(".//*[@class='product_page']/p/text()").extract()     

        # Product advance informations
        product_upc = product_info(response, 'UPC')
        
        dict_item = []

        if product_name and product_price and product_rating and product_desc and product_upc:
            dict_item += [dict_item]
        
    	


            yield {
                'Product Name':product_name,
                'Product Price': product_price,
                'Product Rating': product_rating,
                'Product About': product_desc,

                'Product UPC':product_upc
            }