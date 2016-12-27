# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import db
import json
from guazi_car_source.items import GuaziCarSourceItem,CarItem
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class GuaziCarSourcePipeline(object):
	def __init__(self):
		self.file = codecs.open('city.json', 'w', encoding='utf-8')
		self.file2 = codecs.open('carsource.json', 'w', encoding='utf-8')

	def spider_closed(self, spider):
		self.file.close()

	def process_item(self, item, spider):
		if isinstance(item,GuaziCarSourceItem):
			line = json.dumps(dict(item), ensure_ascii=False) + "\n"
			self.file.write(line)
		if isinstance(item,CarItem):
			line = json.dumps(dict(item),ensure_ascii=False) + "\n"
			self.file2.write(line)
		return item
