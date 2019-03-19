# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import sys
import django

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

sys.path.append(os.path.join(BASE_DIR, 'store'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'store.settings'
django.setup()

from goods.tasks import save_goods_to_db


class ScraperPipeline(object):

    def __init__(self):
        super(ScraperPipeline, self).__init__()
        self.items_list = []

    def process_item(self, item, spider):
        self.items_list.append(item)
        print("*" * 20)
        print("*" * 20)
        print('COUNT:{}'.format(len(self.items_list)))
        print("*" * 20)
        print("*" * 20)
        if len(self.items_list) == 10:
            print("*"*20)
            print("*" * 20)
            print(self.items_list)
            print("*" * 20)
            print("*" * 20)
            save_goods_to_db.delay(self.items_list)
            self.items_list = []
        return item

