# -*- coding: utf-8 -*-
import scrapy
from wwtyc.settings import COOKIES
import urllib.parse
from wwtyc.items import WwtycItem

class TycWwSpider(scrapy.Spider):
    name = 'tyc_ww'
    allowed_domains = ['tianyancha.com']
    start_urls = ['https://www.tianyancha.com/search?key=']
# https://www.tianyancha.com/search?base=bj&areaCode=110112


    def start_requests(self):
        f = open('list.txt','r',encoding='utf-8')
        for f_out in f:
            company = urllib.parse.quote(f_out)
            url = self.start_urls[0] + company
            yield scrapy.Request(url,cookies=COOKIES,callback=self.parse)

    def parse(self, response):
        follow = response.xpath('//a[@class="name "]/@href').extract_first()
        yield scrapy.Request(follow,cookies=COOKIES,callback=self.page_parse)

    def page_parse(self,response):
        item = WwtycItem()
        #公司名
        item['name'] = response.xpath('//div[@class="content"]/div[@class="header"]/h1/text()').extract_first().strip()
        #电话
        phone = response.xpath('//div[@class="f0"][1]/div[@class="in-block"][1]/span[2]/text()').extract_first()
        item['phone'] = phone.strip() if phone else '暂无电话信息'
        #邮箱
        email = response.xpath('//div[@class="f0"][1]/div[@class="in-block"][2]/span[2]/text()').extract_first()
        item['email'] = email.strip() if email else '暂无邮箱信息'
        #网站地址
        web = response.xpath('//div[@class="f0"][2]/div[@class="in-block"][1]/a/text()').extract_first()
        item['web'] = web.strip() if web else '暂无网址信息'
        #公司地址
        address = response.xpath('//div[@class="f0"][2]/div[@class="in-block"][2]/span[2]/@title').extract_first()
        item['address'] = address.strip() if address else '暂无地址信息'
        #注册资本
        regist_capital = response.xpath('//div[@class="data-content"]/table[1]/tbody/tr[1]/td[2]/div[2]/@title').extract_first()
        item['regist_capital'] = regist_capital.strip() if regist_capital else '暂无注册资本信息'
        #注册时间
        regist_time = response.xpath('//div[@class="data-content"]/table[1]/tbody/tr[2]/td/div[2]/text/text()').extract_first()
        item['regist_time'] = regist_time.strip() if regist_time else '暂无注册时间信息'
        #公司状态
        status = response.xpath('//div[@class="data-content"]/table[1]/tbody/tr[3]/td/div[2]/@title').extract_first()
        item['status'] = status.strip() if status else '暂无公司状态信息'
        # 工商注册号
        business_num = response.xpath('//table[@class="table -striped-col -border-top-none"]/tbody/tr[1]/td[2]/text()').extract_first()
        item['business_num'] = business_num.strip() if business_num else '暂无工商注册号信息'
        # 组织机构代码
        organizing_code = response.xpath('//table[@class="table -striped-col -border-top-none"]/tbody/tr[1]/td[4]/text()').extract_first()
        item['organizing_code'] = organizing_code.strip() if organizing_code else '暂无组织机构代码信息'
        # 统一社会信用代码
        social_code = response.xpath('//table[@class="table -striped-col -border-top-none"]/tbody/tr[2]/td[2]/text()').extract_first()
        item['social_code'] = social_code.strip() if social_code else '暂无统一社会信用代码信息'
        # 公司类型
        company_type = response.xpath('//table[@class="table -striped-col -border-top-none"]/tbody/tr[2]/td[4]/text()').extract_first()
        item['company_type'] = company_type.strip() if company_type else '暂无公司类型信息'
        # 纳税人识别号
        taxpayer_num = response.xpath('//table[@class="table -striped-col -border-top-none"]/tbody/tr[3]/td[2]/text()').extract_first()
        item['taxpayer_num'] = taxpayer_num.strip() if taxpayer_num else '暂无识别号信息'
        # 行业
        industry = response.xpath('//table[@class="table -striped-col -border-top-none"]/tbody/tr[3]/td[4]/text()').extract_first()
        item['industry'] = industry.strip() if industry else '暂无行业信息'
        # 营业期限
        operate_period = response.xpath('//table[@class="table -striped-col -border-top-none"]/tbody/tr[4]/td[2]/span/text()').extract_first()
        item['operate_period'] = operate_period.strip() if operate_period else '暂无营业期限信息'
        # 核准日期
        approval_date = response.xpath('//table[@class="table -striped-col -border-top-none"]/tbody/tr[4]/td[4]/text/text()').extract_first()
        item['approval_date'] = approval_date.strip() if approval_date else '暂无核准日期信息'
        # 纳税人资质
        taxpayer_qua = response.xpath('//table[@class="table -striped-col -border-top-none"]/tbody/tr[5]/td[2]/text()').extract_first()
        item['taxpayer_qua'] = taxpayer_qua.strip() if taxpayer_qua else '暂无纳税人资质信息'
        # 人员规模
        staff = response.xpath('//table[@class="table -striped-col -border-top-none"]/tbody/tr[5]/td[4]/text()').extract_first()
        item['staff'] = staff.strip() if staff else '暂无人员规模信息'
        # 实缴资本
        capitial = response.xpath('//table[@class="table -striped-col -border-top-none"]/tbody/tr[6]/td[2]/text()').extract_first()
        item['capitial'] = capitial.strip() if capitial else '暂无实缴资本信息'
        # 登记机关
        authority = response.xpath('//table[@class="table -striped-col -border-top-none"]/tbody/tr[6]/td[4]/text()').extract_first()
        item['authority'] = authority.strip() if authority else '暂无登记机关信息'
        # 参保人数
        insured_num = response.xpath('//table[@class="table -striped-col -border-top-none"]/tbody/tr[7]/td[2]/text()').extract_first()
        item['insured_num'] = insured_num.strip() if insured_num else '暂无参保人数信息'
        # 英文名称
        english_name = response.xpath('//table[@class="table -striped-col -border-top-none"]/tbody/tr[7]/td[4]/text()').extract_first()
        item['english_name'] = english_name.strip() if english_name else '暂无英文名信息'
        # 注册地址
        regist_add = response.xpath('//table[@class="table -striped-col -border-top-none"]/tbody/tr[8]/td[2]/text()').extract_first()
        item['regist_add'] = regist_add.strip() if regist_add else '暂无注册地址信息'
        # 经营范围
        scope = response.xpath('//table[@class="table -striped-col -border-top-none"]/tbody/tr[9]/td[2]/span/span/span/text()').extract_first()
        item['scope'] = scope.strip() if scope else '暂无经营范围信息'

        yield item





