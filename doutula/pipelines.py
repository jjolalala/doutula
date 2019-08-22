# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv


class DoutulaPipeline(object):

    #可选
    def __init__(self):
        self.filename = open('tc.csv', 'w', encoding='gbk')

    def process_item(self, item, spider):
        txt = str(dict(item)) + ',\n'
        self.filename.write(txt)
        return item

    #可选
    def close_spider(self, spider):
        self.filename.close()