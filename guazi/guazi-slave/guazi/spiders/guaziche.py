# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider

from scrapy.selector import Selector
from guazi.items import GuaziItem
import time
import code
values = {
           "国一": 1,
           "国二": 2,
           "国三": 3,
           "国四": 4,
           "国五": 5
         }


class GuazicheSpider(RedisSpider):
    name = "guaziche"
    allowed_domains = ["guazi.com"]
    redis_key = 'guazi:car_urls'

    def parse(self, response):
        sel = Selector(response)
        item = GuaziItem()
        item['sourceSite'] = 1
        item['carCityZhId'] = sel.xpath("//a[@class='logo']/@href")[0].extract()
        item['price'] = sel.xpath("//div[@class='pricebox']/span[1]/b/text()")[0].extract()[1:]
        if len(sel.xpath("//div[@class='pricebox']/span[2]/font[1]/text()")) ==0:
            item['newPrice'] = ""
        else:
            item['newPrice'] = sel.xpath("//div[@class='pricebox']/span[2]/font[1]/text()")[0].extract()
            if len(sel.xpath("//div[@class='con-param']")) ==0:
                item['discharge'] = 0
            else:
                item['discharge'] = sel.xpath("//div[@class='con-param']/div/div[2]/table/tr[2]/td[2]/text()")[0].extract()
                miles = sel.xpath("//ul[contains(@class,'assort')]/li[2]/b/text()")[0].extract()
                item['miles'] = miles[0:len(miles)-3]
                item['gearBox'] = sel.xpath("//ul[contains(@class,'assort')]/li[3]/b/text()")[0].extract()
                item['title'] = sel.xpath("//div[contains(@class,'det-sumright')]/div[1]/h1/text()")[0].extract()
                item['descStr'] = sel.xpath("//div[@id='base']/p/text()")[0].extract()
                emission = sel.xpath("//ul[contains(@class,'assort')]/li[4]/b/text()")[0].extract()
                item['emission'] = values.get(emission,5)
                item['carCityZh'] = sel.xpath("//ul[contains(@class,'assort')]/li[5]/b/text()")[0].extract()
                item['licenseDate'] = sel.xpath("//ul[contains(@class,'assort')]/li[1]/b/text()")[0].extract()
                item['carSrcUrl'] = response.url
                print response.url.encode('GB18030')
                print item['carCityZhId'].encode('GB18030')
                item['carSrcId'] = response.url.strip('https://www.guazi.com').strip(item['carCityZhId']).strip('.htm')
                print item['carSrcId']
        # item['carSrcId'] = sel.xpath("//div[@class='car-fuwu'][1]/@data-puid")[0].extract()
        item['tel'] = sel.xpath("//p[@class='stipul-p']/span/b/text()")[0].extract()
        item['transferNum'] = sel.xpath("//div[@id='base']/ul/li[@class='guohu']/text()")[0].extract()
        item['detected'] = 0
        item['personal'] = 0
        grayBtn = sel.xpath("//p[@class='stipul-p']/a[contains(@class,'stipul-btn-gray')]")
        item['status'] = 1 #正常
        if len(grayBtn)>0:
            item['status'] =2 #已下架
        item['visitTime'] =int(time.time())
        item['publishDate'] = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        item['lockUserId'] = 0
        item['carFingerHash'] = str(time.time())+"hello"
        item['imgStr'] = ''
        imgs = sel.xpath("//ul[@class='det-picside']/li/img/@src")
        if len(imgs) > 0:
            item['firstImgStr'] = imgs[0].extract()
            for img in imgs:
                item['imgStr'] += img.extract()+'///'
        return item


