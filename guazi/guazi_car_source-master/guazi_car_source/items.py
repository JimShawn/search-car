# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GuaziCarSourceItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    cityName = scrapy.Field()
    cityShortWord = scrapy.Field()
    pass

class CarInfoItem(scrapy.Item):
	"""docstring for CarInfoItem"""
	carDetail = scrapy.Field()
	yearMonth = scrapy.Field()
	miles = scrapy.Field()
	price = scrapy.Field()
	newCarPrice = scrapy.Field()
	city = scrapy.Field()
	source = scrapy.Field()
	dataCarId = scrapy.Field()

class CarItem(scrapy.Item):
	"""docstring for CarInfoItem"""
	carid = scrapy.Field()
	carurl = scrapy.Field()
