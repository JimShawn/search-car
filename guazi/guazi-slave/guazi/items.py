# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GuaziItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	sourceSite = scrapy.Field()
	carCityZhId = scrapy.Field()
	price = scrapy.Field()
	newPrice = scrapy.Field()
	discharge = scrapy.Field()
	miles = scrapy.Field()
	gearBox = scrapy.Field()
	title = scrapy.Field()
	descStr = scrapy.Field()
	emission = scrapy.Field()
	carCityZh = scrapy.Field()
	licenseDate = scrapy.Field()
	carSrcUrl = scrapy.Field()
	carSrcId = scrapy.Field()
	tel = scrapy.Field()
	status = scrapy.Field()
	transferNum = scrapy.Field()
	detected = scrapy.Field()
	personal = scrapy.Field()
	visitTime = scrapy.Field()
	publishDate = scrapy.Field()
	lockUserId = scrapy.Field()
	carFingerHash = scrapy.Field()
	firstImgStr = scrapy.Field()
	imgStr = scrapy.Field()

