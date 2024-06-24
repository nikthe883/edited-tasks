
# imports

import scrapy
import json
from ..product_extractor import ProductExtractor

class ProductSpider(scrapy.Spider):
    name = "product_spider"
    start_urls = ['https://www.marksandspencer.com/bg/easy-iron-geometric-print-shirt/p/P60639302.html']

    def parse(self, response):

        # Extract the JSON-LD script tag content
        json_ld_data = response.xpath('//script[@type="application/ld+json"]/text()').getall()
        
        # Parse the JSON data
        product_data_j = json.loads(json_ld_data[1])
        
        # Collect product_data
        product_data = {
            'name': ProductExtractor.extract_name_css(response),
            'price': ProductExtractor.extract_price_css(response),
            'colour': ProductExtractor.extract_colour_css(response),
            'size': ProductExtractor.extract_sizes_css(response),
            'reviews_count_text' : ProductExtractor.extract_reviews_count_text_json(product_data_j),
            'reviews_score': ProductExtractor.extract_reviews_score_text_json(product_data_j)
        }


        yield product_data