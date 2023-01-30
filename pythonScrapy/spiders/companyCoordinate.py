import scrapy
from scrapy_selenium import SeleniumRequest

class CompanycoordinateSpider(scrapy.Spider):
    name = 'companyCoordinate'
    allowed_domains = ['www.google.com.tw']
    url = 'https://www.google.com/maps/place/235%E6%96%B0%E5%8C%97%E5%B8%82%E4%B8%AD%E5%92%8C%E5%8D%80%E4%B8%AD%E6%AD%A3%E8%B7%AF716%E8%99%9F'
    def start_requests(self):
        yield SeleniumRequest(
            url=self.url,
            callback=self.parse,
            wait_time=10)
    def parse(self, response):
        search = response.css("div.onegoogle").getall()
        print(search)
