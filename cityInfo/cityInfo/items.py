# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CityinfoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    address = scrapy.Field()
    province = scrapy.Field()
    citycode = scrapy.Field()
    city = scrapy.Field()
    adcode = scrapy.Field()
    location = scrapy.Field()
    level = scrapy.Field()
    district = scrapy.Field()