# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy import log
from scrapy.http import Request
import random
import subprocess
import time
import re
import json
from redis import Redis

from guazi_car_source.items import GuaziCarSourceItem,CarItem

class CarSourceSpider(scrapy.Spider):
    name = "car-source"
    allowed_domains = ["guazi.com"]
    
    start_urls = ["https://www.guazi.com/www/"]
    # doneCityNum = 0
    # start_urls.append(url)
    

    

    def parse(self, response):
        print 'hello'
        sel = Selector(response)
        cityDls = sel.xpath("//div[contains(@class,'all-city')]/dl")[1:]
        for cityDl in cityDls:
            cityAs = cityDl.xpath("dd/a")
            
            # yield Request('http://www.guazi.com/bj/buy/o1/',meta={'startNumber':1,'cityShortWord':'/bj/','cityName':'北京'},callback=self.__get_car_source)
            for cityA in cityAs:
                cityName = cityA.xpath("text()")[0].extract().strip().rstrip().lstrip()
                cityShortWord = cityA.xpath("@href")[0].extract()
                item = GuaziCarSourceItem()
                item['cityName'] = cityName
                item['cityShortWord'] = cityShortWord
                yield item
                carSourcePageUrl = "http://www.guazi.com"+cityShortWord+"buy/o1/"
                print carSourcePageUrl
                yield Request(carSourcePageUrl,meta={'startNumber':1,'cityShortWord':cityShortWord,'cityName':cityName},callback=self.__get_car_source)
            

    def __get_car_source(self,response):
        sel = Selector(response)
        startNumber = response.meta['startNumber']
        cityShortWord = response.meta['cityShortWord']
        cityName = response.meta['cityName']
        r = Redis()
        
        startNumberInt = int(startNumber)
        totalPagesInt = 50
        if startNumber>totalPagesInt:
            return

        carInfoDivs = sel.xpath("//ul[contains(@class,'list-bigimg') and contains(@class,'clearfix')]/li/div")
        for carInfoDiv in carInfoDivs:
            item = CarItem()
            position = carInfoDiv.xpath("p/span[contains(@class,'tag-gray')]")
            if len(position) == 1:#表示当前数据是其他城市的车了，无需爬取
                return;
            carDetail = 'https://www.guazi.com'+carInfoDiv.xpath("p/a/@href")[0].extract()
            dataCarId = carInfoDiv.xpath("p/a/@href")[0].extract().strip(cityShortWord).strip('.htm')
            
            # yearMonth = carInfoDiv.xpath("p[2]/span/text()")[0].extract().strip()
            # miles = carInfoDiv.xpath("p[contains(@class,'fc-gray')]/descendant::text()").extract()[-1].strip()
            # price = carInfoDiv.xpath("p[3]/span/i/text()")[0].extract().strip()
            # newCarPriceDiv = carInfoDiv.xpath("p[3]/s/text()")
            # if len(newCarPriceDiv) == 0:
            #     newCarPrice = '暂无'
            # else:
            #     newCarPrice = newCarPriceDiv[0].extract().strip()
            # item['carDetail'] = carDetail
            # item['yearMonth'] = yearMonth
            # item['price'] = price.strip().lstrip().rstrip('\n')
            # item['miles'] = miles
            # item['newCarPrice'] = newCarPrice
            # item['city'] = cityName
            # item['dataCarId'] = dataCarId
            # item['source'] = 'guazi'
            item['carid'] = dataCarId
            item['carurl'] = carDetail
            r.lpush('guazi:car_urls', carDetail)
        
        nextPageUrl = "http://www.guazi.com"+cityShortWord+"buy/o"+str(startNumber+1)+"/"
        print nextPageUrl
        yield Request(nextPageUrl,meta={'startNumber':startNumber+1,'cityShortWord':cityShortWord,'cityName':cityName},callback=self.__get_car_source)

        
        

            
    
            
            
        
    
           