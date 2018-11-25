# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WwtycItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    phone = scrapy.Field()
    email = scrapy.Field()
    address = scrapy.Field()
    web = scrapy.Field()
    regist_capital = scrapy.Field()
    regist_time = scrapy.Field()
    status = scrapy.Field()
    business_num = scrapy.Field()         #工商注册号
    organizing_code = scrapy.Field()      #组织机构代码
    social_code = scrapy.Field()          #统一社会信用代码
    company_type = scrapy.Field()         #公司类型
    taxpayer_num = scrapy.Field()         #纳税人识别号
    industry = scrapy.Field()             #行业
    operate_period = scrapy.Field()       #营业期限
    approval_date = scrapy.Field()        #核准日期
    taxpayer_qua = scrapy.Field()         #纳税人资质
    staff = scrapy.Field()                #人员规模
    capitial = scrapy.Field()             #实缴资本
    authority = scrapy.Field()            #登记机关
    insured_num = scrapy.Field()          #参保人数
    english_name = scrapy.Field()         #英文名称
    regist_add = scrapy.Field()           #注册地址
    scope = scrapy.Field()                #经营范围

class LawsuitItem(scrapy.Item):
    name = scrapy.Field()
    date = scrapy.Field()
    event_name = scrapy.Field()
    cause = scrapy.Field()
    status = scrapy.Field()
    case_num = scrapy.Field()
    detail = scrapy.Field()