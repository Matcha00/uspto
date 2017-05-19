# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from uspto.items import UsptoItem
from uspto.spiders.uspto_spider import keyword

class UsptoPipeline(object):
    def __init__(self):
        clinet = pymongo.MongoClient("localhost", 27017)
        db_name = input("name:")
        db = clinet["UsptoHub"]
        print(keyword)
        self.PhRes = db[db_name]

    def process_item(self, item, spider):
        print('MongoDBItem', item)

        while "\n" in item['abstract']:
            item['abstract'].remove("\n")
        """ 判断类型 存入MongoDB """
        if isinstance(item, UsptoItem):
            print ('PornVideoItem True')
            try:
                self.PhRes.update({'us_patent_id': item['us_patent_id']}, {'$set': dict(item)}, True)
            except Exception:
                pass
        return item
