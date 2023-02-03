# Scrapy settings for pythonScrapy project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'pythonScrapy'

SPIDER_MODULES = ['pythonScrapy.spiders']
NEWSPIDER_MODULE = 'pythonScrapy.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'pythonScrapy (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 1

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 5
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 1
CONCURRENT_REQUESTS_PER_IP = 1

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'pythonScrapy.middlewares.PythonscrapySpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'scrapy_selenium.SeleniumMiddleware': 800,
   'pythonScrapy.middlewares.PythonscrapyDownloaderMiddleware': 543,
   'pythonScrapy.middlewares.RandomUserAgentMiddleware':542,
   'pythonScrapy.middlewares.AddRequestHeaderMiddleware':541,
   'pythonScrapy.middlewares.RandomDelayMiddleware':150,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'pythonScrapy.pipelines.PythonscrapyPipeline': None,
   'pythonScrapy.pipelines.CompanyCoordinatePipeline' : 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

#-------------------------------------Not Scrapy Begin Settings-------------------------------------------------------

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = '2.7'
TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'

#Set Selenium Parameter Here
SELENIUM_DRIVER_NAME = 'chrome'  # 瀏覽器名稱
SELENIUM_DRIVER_EXECUTABLE_PATH = 'chromedriver.exe'  # 驅動程式路徑
SELENIUM_DRIVER_ARGUMENTS = ['-headless']

#Set LOG File Here
LOG_FILE = 'companyCoLog.txt'

#Set Headers in here
HEADERS = {
   'Accept': '*/*',
   'Accept-Encoding': 'gzip, deflate, br',
   'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
   'Connection':'keep-alive',
   'Cookie': '__gads=ID=365971df3763d46d-225b41ad58d900c4:T=1674116223:RT=1674116223:S=ALNI_MYgEHsnUNqji8FasLeEFpNOaU3RBQ; ASPSESSIONIDQUQABTSR=BLFBJLLDDNNEMJFFFDEHCNKG; ASP.NET_SessionId=20bdom4ycrypr0txpzgnnb3u; ASPSESSIONIDQUSCBSSQ=LACJMEMDBINAALICLKIGIOEC; ASPSESSIONIDSWSBATTR=KAFLNKDAOEEAFGDNHGBLMLJA; ASPSESSIONIDQUQADTSR=PIOHLJFACCJJPIPGPFJOJENF; ASPSESSIONIDQWQBCSSQ=PHKHMHGADPFIAKPPDDMBGCCO; ASPSESSIONIDQQRAASTR=CGADCLGADPDBKLOBMEPPPNKP; ASPSESSIONIDQWSCBSTR=PKAPCLGAGAAMJPHHEMJEPEGN; ASPSESSIONIDSWTBBQQS=NBGLCNHAOIEAMHCPHKLPAFLF; ASPSESSIONIDSSTBBRTQ=GPELPMHAGBLEJLKDCHIJEBJB; ASPSESSIONIDSSSCBRSQ=GHKDNNHALIOCEFMONJOEDINA; ASPSESSIONIDSQRBDRTQ=EKHHNPHAFKLECEPGMOMBBECP; ASPSESSIONIDQQQBARSR=MGNJLAIABIGBNPONGJCBAKAN; ASPSESSIONIDQSQBATSR=FGOFFDIAOOMMPJKDBJKFNLCP; ServerName=www%2Emap%2Ecom%2Etw; ASPSESSIONIDQWQABTSR=NIBLBHNACFJBHPCKNANOGAFN; __gpi=UID=00000ba7cc715de7:T=1674116223:RT=1675211446:S=ALNI_MbM65kz7Z7nQ5FqaHEHVOFY5k6LXw; ASPSESSIONIDQURCBRTR=DBCFKJNAEEEFLIEOLPCNOGJB; ASPSESSIONIDQUTCAQTQ=HNDJOJNAENCOGNGLAABIFCLB; ASPSESSIONIDSWRACQSR=JMKJPKNALPNMOPOOIPKPDPPH',
   'Referer': 'https://www.map.com.tw/',
   'Host' : 'api.map.com.tw',
   'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
   'sec-ch-ua-mobile': '?0',
   'sec-ch-ua-platform': '"Windows"',
   'Sec-Fetch-Dest':'script',
   'Sec-Fetch-Mode':'no-cors',
   'Sec-Fetch-Site':'same-site',
}
#-----------------------------------------companyCoordinate Settings------------------------------------------------
#SetDataPathHere
COORDINATE_PATH_SETTINGS = {
   "importDir": "D:\\工業區-廠商\\工業區\\111年進出口廠商清冊\\111年進出口廠商清冊爬蟲\\座標爬蟲\\",
   "importFile": "111年生產中工廠清冊爬蟲(和工廠資料比對完).xlsx"
}
#Set Config Path Here
COORDINATE_CONFIG_PATH = "D:\\pythonScrapy\\pythonScrapy\\config\\companyCoordinate\\"
#Set CompanyCoordinate Data Start And End Scrapy Here
COORDINATE_DATA_START = 0
COORDINATE_DATA_END = 10

#Set Used CompanyCoordinate Data Column Here
COORDINATE_USE_COLUMN = ["公司名稱","統一編號","公司地址"]

#Set CompanyCoordinate CompanyName Column Here
COORDINATE_COMNAME_COLUMN = "公司名稱"

#Set CompanyCoordinate CompanyTaxNum Column Here
COORDINATE_COMTAXID_COLUMN = "統一編號"

#Set CompanyCoordinate CompanyAddress Column Here
COORDINATE_COMADD_COLUMN = "公司地址"

# Set CompanyCoordinate UrlHead Here
COORDINATE_URLHEAD = "https://api.map.com.tw/net/GraphicsXY_TWMAP.aspx?search_class=address&searchkey=32FAFAA12E07573A06C6BAFFCC206D162C7C9D49&fun=funA&SearchWord="

#Set CompanyCoordinate Error Try
COORDINATE_MAX_ERR_TRY = 2