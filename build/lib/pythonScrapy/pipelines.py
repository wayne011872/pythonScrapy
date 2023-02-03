# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pythonGeneral.database.mongo as pm
from pythonScrapy.libs.companyCoordinate.lib_scrapy import getConfigDir
from pythonScrapy.libs.companyCoordinate.lib_scrapy import getDictItems

class PythonscrapyPipeline:
    def process_item(self, item, spider):
        return item

class CompanyCoordinatePipeline:
    def __init__(self):
        configDir = getConfigDir()
        self.mon = pm.mon(configDir)
    
    def process_item(self,item,spider):
        itemsDict = getDictItems(item)
        print(itemsDict)
        self.mon.insertOneData(itemsDict)
        return item