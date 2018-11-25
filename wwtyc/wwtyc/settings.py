# -*- coding: utf-8 -*-

# Scrapy settings for wwtyc project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'wwtyc'

SPIDER_MODULES = ['wwtyc.spiders']
NEWSPIDER_MODULE = 'wwtyc.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 2
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'www.tianyancha.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36",
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'wwtyc.middlewares.WwtycSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'wwtyc.middlewares.WwtycDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'wwtyc.pipelines.WwtycPipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
COOKIES = {'TYCID': '2e9b4180d33e11e8a43013619f7d13d7', 'undefined': '2e9b4180d33e11e8a43013619f7d13d7', 'ssuid': '4262972438', '_ga': 'GA1.2.409416134.1539912472', '_gid': 'GA1.2.51127275.1542678613', 'RTYCID': '6babaa8d16f54470b2755b17439ff3cb', 'CT_TYCID': '3bec4880b68345e0b10a5c8790cb15bd', 'tyc-user-info': '%257B%2522myQuestionCount%2522%253A%25220%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522monitorUnreadCount%2522%253A%252226%2522%252C%2522discussCommendCount%2522%253A%25221%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODMwMzAxODQ2MiIsImlhdCI6MTU0MjY3ODY3OSwiZXhwIjoxNTU4MjMwNjc5fQ.Vz3AsYHj3AtAuNaUyQkAzA3cO3D9OHsecDS5hiN9jXi5dTKEX9oRTNy3b1Zl_wgh38a17ffX8FD-IdjBd9etlA%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522pleaseAnswerCount%2522%253A%25221%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522mobile%2522%253A%252218303018462%2522%257D', 'auth_token': 'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODMwMzAxODQ2MiIsImlhdCI6MTU0MjY3ODY3OSwiZXhwIjoxNTU4MjMwNjc5fQ.Vz3AsYHj3AtAuNaUyQkAzA3cO3D9OHsecDS5hiN9jXi5dTKEX9oRTNy3b1Zl_wgh38a17ffX8FD-IdjBd9etlA', 'aliyungf_tc': 'AQAAAH/0ex1PdAgA8g/QZ/0ykhnlC+eZ', 'csrfToken': 'btU5wE6eRGytNC34th7EifG5', 'Hm_lvt_e92c8d65d92d534b0fc290df538b4758': '1542678614,1542700716,1542711764', 'bannerFlag': 'true', 'Hm_lpvt_e92c8d65d92d534b0fc290df538b4758': '1542712300', 'cloud_token': 'b2003d7b9ef3492cbe8a68ef5240ef9b'}



