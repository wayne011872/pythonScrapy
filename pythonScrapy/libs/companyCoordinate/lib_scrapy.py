from pythonScrapy.settings import COORDINATE_DATA_START
from pythonScrapy.settings import COORDINATE_DATA_END
from pythonScrapy.settings import COORDINATE_USE_COLUMN
from pythonScrapy.settings import COORDINATE_COMNAME_COLUMN
from pythonScrapy.settings import COORDINATE_COMTAXID_COLUMN
from pythonScrapy.settings import COORDINATE_COMADD_COLUMN
from pythonScrapy.settings import COORDINATE_URLHEAD
from pythonScrapy.settings import COORDINATE_PATH_SETTINGS
from pythonScrapy.settings import COORDINATE_MAX_ERR_TRY
from pythonScrapy.settings import COORDINATE_CONFIG_PATH
import pythonGeneral.dataProcessing.string as pds

def getDataPath():
    path_settings = {}
    importDir = COORDINATE_PATH_SETTINGS.get("importDir")
    importFile = COORDINATE_PATH_SETTINGS.get("importFile")
    exportDir = COORDINATE_PATH_SETTINGS.get("exportDir")
    exportFile = COORDINATE_PATH_SETTINGS.get("exportFile")
    path_settings['importDir'] = importDir
    path_settings['importFile'] = importFile
    path_settings['exportDir'] = exportDir
    path_settings['exportFile'] = exportFile
    return path_settings

def getStartDataNum():
    startDataNum = COORDINATE_DATA_START
    return startDataNum

def getEndDataNum():
    endDataNum = COORDINATE_DATA_END
    return endDataNum

def getUsedCol():
    usedCol = COORDINATE_USE_COLUMN
    return usedCol

def getComNameCol():
    comName = COORDINATE_COMNAME_COLUMN
    return comName

def getComTaxIDCol():
    comTaxID = COORDINATE_COMTAXID_COLUMN
    return comTaxID

def getComAddrCol():
    comAddr = COORDINATE_COMADD_COLUMN
    return comAddr

def getUrlHead():
    urlHead = COORDINATE_URLHEAD
    return urlHead

def getErrorTryNum():
    errorTryNum = COORDINATE_MAX_ERR_TRY
    return errorTryNum

def setItems(item, taxIdNum,companyName,companyLatitude, companyLongitude):
    item["taxIdNum"] = taxIdNum
    item["companyName"] = companyName
    item["latitude"] = companyLatitude
    item["longitude"] = companyLongitude
    return item
    
def getConfigDir():
    configDir = COORDINATE_CONFIG_PATH
    return configDir

def getDictItems(item):
    longitudeRe = pds.reString(item['longitude'])
    latitudeRe = pds.reString(item["latitude"])
    itemDict = {}
    coordinateList = []
    coordinateList.append(float(longitudeRe.deleteSpace()))
    coordinateList.append(float(latitudeRe.deleteSpace()))
    positionDict = {}
    positionDict["type"] = "Point"
    positionDict["coordinates"] = coordinateList
    itemDict["companyName"] = pds.deleteSpace(item['companyName'])
    itemDict["taxIdNum"] = pds.deleteSpace(item['taxIdNum'])
    itemDict["position"] = positionDict
    return itemDict

def getResponseCompanyName(spider,headerCount):
    resCompanyName = str(spider.myDfData.df.at[headerCount, spider.companyNameCol])
    return resCompanyName

def getResponseTaxIdNum(spider,headerCount):
    resTaxIdNum = str(spider.myDfData.df.at[headerCount, spider.companyTaxIdCol])
    return resTaxIdNum