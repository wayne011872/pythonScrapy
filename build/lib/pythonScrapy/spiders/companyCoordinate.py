import scrapy
import orjson
import logging
from pythonScrapy.items import CompanyCoordinateItem
import pythonScrapy.libs.companyCoordinate.lib_scrapy as ccls
import pythonGeneral.dataProcessing.pandas as pds

class CompanycoordinateSpider(scrapy.Spider):
    name = 'companyCoordinate'
    count = 0
    
    def setDataSettings(self):
        self.urlHead = ccls.getUrlHead()
        self.startNum = ccls.getStartDataNum()
        self.endNum = ccls.getEndDataNum()
        self.usedColumn = ccls.getUsedCol()
        self.companyNameCol = ccls.getComNameCol()
        self.companyTaxIdCol = ccls.getComTaxIDCol()
        self.companyAddrCol = ccls.getComAddrCol()
        self.maxErrTry = ccls.getErrorTryNum()
        self.path_settings = ccls.getDataPath()
        self.myDfData = pds.df_data(self.path_settings,useColumns=self.usedColumn)
    
    def setRequestUrl(self,requestCount):
        requestAddress = ccls.getRequestAddress(self,requestCount)
        requestUrl = self.urlHead+requestAddress
        return requestUrl
        
    def start_requests(self):
        self.setDataSettings()
        for self.count in range(self.startNum,self.endNum):
            requestUrl = self.setRequestUrl(self.count)
            yield scrapy.Request(
                url=requestUrl,
                callback=self.parse
                )

    def parse(self, response):
        item = CompanyCoordinateItem()
        headerCount = int(str(response.request.headers['Count']).split("'")[1])
        resCompanyName = ccls.getResponseCompanyName(self,headerCount)
        resTaxIdNum = ccls.getResponseTaxIdNum(self,headerCount)
        
        try:
            responseData = str(response.text).split("(")[1]
            responseData = str(responseData).split(")")[0]
        except:
            item = ccls.setItems(item, resTaxIdNum, resCompanyName, "0", "0")
            responseTextErr = "[{0}] {1} responseText 沒有或出問題".format(headerCount, resTaxIdNum)
            print(responseTextErr)
            logging.error(responseTextErr)
        else:
            try:
                companyLatitude = orjson.loads(responseData)["locate"]["lat"]
                companyLongitude = orjson.loads(responseData)["locate"]["lng"]
            except:
                item = ccls.setItems(item, resTaxIdNum, resCompanyName, "0", "0")
                orjsonErr = "[{0}] {1} orjson loads出問題".format(headerCount, resTaxIdNum)
                print(orjsonErr)
                logging.error(orjsonErr)
            else:
                if companyLatitude == '0' or companyLongitude == '0':
                    item = ccls.setItems(item, resTaxIdNum, resCompanyName, "0", "0")
                    noDataErr = "[{0}] {1} 經緯度資料為0".format(headerCount, resTaxIdNum)
                    print(noDataErr)
                    logging.error(noDataErr)
                else:
                    item = ccls.setItems(item, resTaxIdNum, resCompanyName, companyLatitude, companyLongitude)
                    dataMessage = "[{0}] taxId: {1} \nlatitude:{2} longitude:{3}".format(headerCount, resTaxIdNum, companyLatitude, companyLongitude)
                    print(dataMessage)
                    logging.info(dataMessage)
        yield item