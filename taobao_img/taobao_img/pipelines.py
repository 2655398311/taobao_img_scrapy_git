# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from taobao_img.settings import MONGODB_HOST,MONGODB_PORT,MONGODB_DBNAME,MONGODB_DOCNAME
import pymongo


class TaobaoImgPipeline(object):

    def __init__(self):

        #数据库连接
        host = MONGODB_HOST
        port = MONGODB_PORT
        dbname = MONGODB_DBNAME
        client = pymongo.MongoClient(host=host, port=port)
        tdb = client[dbname]
        self.post = tdb[MONGODB_DOCNAME]  # 表名

    # @classmethod
    # def from_crawler(cls, crawler):
    #     print("-----------------------------------")
    #     return cls()
    def process_item(self, item, spider):
        print(item)
        postitem = dict(item)
        # # print(postitem)
        self.post.insert(postitem)
        # print(item)
        return item
