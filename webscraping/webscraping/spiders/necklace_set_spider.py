import scrapy
from ..items import WebscrapingItem

class NecklaceSetSpiderSpider(scrapy.Spider):
    name = 'necklace.set_spider'
    start_urls = [
        'https://www.houseofindya.com/zyra/necklace-sets/cat'
        ]

    def parse(self, response):
        items = WebscrapingItem()

        description = response.css('#JsonProductList p::text').extract()
        price = response.css('#JsonProductList span:nth-child(1)').css('::text').extract()
        image_url = response.css('#JsonProductList .lazy').css('::attr(src)').extract()
        
        items['description'] = description 
        items['price'] = price
        items['image_url'] = image_url

        yield items 

