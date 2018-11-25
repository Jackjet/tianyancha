# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class WwtycPipeline(object):
    number_map = {'8': '0', '6': '1', '7': '2', '1': '3', '4': '4', '0': '5', '3': '6', '2': '7', '5': '8', '9': '9','-':'-'}
    def process_item(self, item, spider):
        check_data = ''
        for i in item['approval_date']:
            check_data += self.number_map[i]
        item['approval_date'] = check_data

        regist = ''
        for j in item['regist_time']:
            regist += self.number_map[j]
        item['regist_time'] = regist
        return item
