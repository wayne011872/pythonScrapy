# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PythonscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class CompanyCoordinateItem(scrapy.Item):
    companyName = scrapy.Field()
    taxIdNum = scrapy.Field()
    latitude = scrapy.Field()
    longitude = scrapy.Field()