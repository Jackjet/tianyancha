# -
使用scrapy框架爬取天眼查网站上公司的基本信息
## 前方
&ensp;&ensp;&ensp;&ensp;本文如有错误或改进之处，望大家提出。
## 背景
&ensp;&ensp;&ensp;&ensp;前面介绍了网站企查查的爬取，详细博文请点击链接查看，具体链接为https://blog.csdn.net/xue605826153/article/details/83933449
&ensp;&ensp;&ensp;&ensp; 天眼查网站的具体爬取思路和企查查是一样的，但是与企查查相比，天眼查的反爬手段更高明。频繁访问会需要输入验证码，而博主现在的水平还解决不了。即使作用代理IP，加大下载延迟等也会被网站发现，所以现在只能做到单次爬取少量公司的信息。
## 码上分析
&ensp;&ensp;&ensp;&ensp;前面提到，天眼查的大概思路与企查查是一样的：首先通过构建IP进入到查询公司的列表页，然后提取出公司详情页的链接，进而访问，进入到详情页后能过xpath提取自己所需要的字段信息。同样，在天眼查中也需要使用cookie登录。              
1.观察链接，构造，进入查询列表页。                      
2.通过xpath提出列表页中首家公司的链接（ps:如果查询时给出的公司名为全名，那么一般 是在列表页的第一个），并访问。                                                 
3.进行详情页后即可提取所要的字段信息了，但是事情总不能尽如人所愿，优秀的开发人员对一些字段进行了加密（注册时间，核准日期），不过现在我自己的解决办法只能是多看几个日期，找到具体的对应，例如，2还是原来的2，0依然是0，1被换成了8......而且这个对应关系是每天一换的。找到具体的对应关系可以在spider中将日期修改为正确的，也可以在pipeline中修改。                               
4.代码
  ```
    # -*- coding: utf-8 -*-
	import scrapy
	from wwtyc.settings import COOKIES
	import urllib.parse
	from wwtyc.items import WwtycItem

	class TycWwSpider(scrapy.Spider):
  	    name = 'tyc_ww'
    	allowed_domains = ['tianyancha.com']
    	start_urls = ['https://www.tianyancha.com/search?key=']
    	
    def start_requests(self):
        f = open('list.txt','r',encoding='utf-8')
        for f_out in f:
            company = urllib.parse.quote(f_out)
            url = self.start_urls[0] + company
            yield scrapy.Request(url,cookies=COOKIES,callback=self.parse)   
    
    #进入查询详情页
    def parse(self, response):
        follow = response.xpath('//a[@class="name "]/@href').extract_first()
        yield scrapy.Request(follow,cookies=COOKIES,callback=self.page_parse)
    
    #进入查询列表页
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
    ```
为了熟悉pipeline,我将数字对应的部分写在了pipeline中。参考时请注意数字对应可能和诸位查看当日的不一样。
    ```
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
    ```
