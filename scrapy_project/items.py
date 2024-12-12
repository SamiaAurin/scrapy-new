# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class ScrapyProjectItem(scrapy.Item):
    Url = scrapy.Field()
    Image = scrapy.Field()
    Name = scrapy.Field()
    Price = scrapy.Field()
