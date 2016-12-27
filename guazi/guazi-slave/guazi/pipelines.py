# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from guazi.items import GuaziItem
import db
import sys
from scrapy import log
reload(sys)
type = sys.setdefaultencoding('utf8')
car_source_pool = db.init_db_pool('db')

class GuaziPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item,GuaziItem):
            try:
                db = car_source_pool.connection()
                cursor = db.cursor()
                sql = """INSERT INTO `CAR` (`source_site`,`city_id`,`price`,`new_price`,`discharge`,`miles`,`gear_box`,`title`,`desc_str`,`emission`,`car_city_zh`,`license_date`,`car_src_url`,`car_src_id`,`tel`,`status`,`transfer_num`,`detected`,`personal`,`visit_time`,`publish_date`,`lock_user_id`,`car_finger_hash`) 
                    VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')""" %(item['sourceSite'],1,
                    item['price'],item['newPrice'],item['discharge'],item['miles'],item['gearBox'],item['title'],
                    item['descStr'],item['emission'],item['carCityZh'],item['licenseDate'],item['carSrcUrl'],item['carSrcId'],
                    item['tel'],item['status'],item['transferNum'],item['detected'],item['personal'],item['visitTime'],
                    item['publishDate'],item['lockUserId'],item['carFingerHash'])
                result = cursor.execute(sql)
                car_id = int(cursor.lastrowid)
                sql2 = """INSERT INTO `car_img` (`car_id`,`first_img_str`,`img_str`)
                     values ('%s','%s','%s')""" %(car_id,item['firstImgStr'],item['imgStr'])
                result2 = cursor.execute(sql2)
                db.commit()
                db.close()
            except Exception as e:
                log.msg("2",level=log.WARNING)
                print e
            finally:
                pass

                return item
