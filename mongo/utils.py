import pymongo
import time
import csv
from buaaac import settings
from mongo import hanlp_process
def getAll():
    myclient = pymongo.MongoClient("mongodb://localhost:27017")
    dblist = myclient.list_database_names()
    if "cloud_academic" not in dblist:
        print("数据库不存在！")
        return 0
    mydb = myclient["cloud_academic"]
    collist = mydb.list_collection_names()
    count = 0
    for str in collist:
        if (str == 'scholar_temp'):
            mycol = mydb[str]
        else:
            continue
        x = mycol.find()
        count += x.count()
    myclient.close()
    return count


def getByOrganizationName(organizationName):
    myclient = pymongo.MongoClient("mongodb://localhost:27017")
    dblist = myclient.list_database_names()
    if "cloud_academic" not in dblist:
        print("数据库不存在！")
        return 0
    mydb = myclient["cloud_academic"]
    collist = mydb.list_collection_names()
    count = 0
    for str in collist:
        if (str == 'scholar_temp'):
            mycol = mydb[str]
        else:
            continue
        x = mycol.find({"organizationName": organizationName})
        count += x.count()
    myclient.close()
    return count


def getByOrganizationNameAndCollegeName(organizationName, collegeName):
    myclient = pymongo.MongoClient("mongodb://localhost:27017")
    dblist = myclient.list_database_names()
    if "cloud_academic" not in dblist:
        print("数据库不存在！")
        return 0
    mydb = myclient["cloud_academic"]
    collist = mydb.list_collection_names()
    count = 0
    for str in collist:
        if (str == 'scholar_temp'):
            mycol = mydb[str]
        else:
            continue
        x = mycol.find({"organizationName": organizationName, "collegeName": collegeName})
        count += x.count()
    myclient.close()
    return count


def getOrganizationNameList(database):
    myclient = pymongo.MongoClient("mongodb://localhost:27017")
    dblist = myclient.list_database_names()
    if "cloud_academic" not in dblist:
        print("数据库不存在！")
        return 0
    mydb = myclient["cloud_academic"]
    collist = mydb.list_collection_names()
    res = []
    for str in collist:
        if (str == database):
            mycol = mydb[str]
        else:
            continue

        res = mycol.distinct('organizationName')
        myclient.close()
        # print(res)
        return res
        # for organization in x:
        #     y = mycol.find({'organizationName':organization}).distinct('collegeName')
        #     z = []
        #     for college in y:
        #         z.append(college)
        #     dict[organization] = z


def getCollegeNameList(database,organizationName):
    myclient = pymongo.MongoClient("mongodb://localhost:27017")
    dblist = myclient.list_database_names()
    if "cloud_academic" not in dblist:
        print("数据库不存在！")
        return 0
    mydb = myclient["cloud_academic"]
    collist = mydb.list_collection_names()
    res = []
    for str in collist:
        if (str == database):
            mycol = mydb[str]
        else:
            continue
        res = mycol.find({"organizationName": organizationName}).distinct('collegeName')
        # print(res)
        myclient.close()
        return res


def getPersonNameList(database,organizationName,collegeName):
    myclient = pymongo.MongoClient("mongodb://localhost:27017")
    dblist = myclient.list_database_names()
    if "cloud_academic" not in dblist:
        print("数据库不存在！")
        return 0
    mydb = myclient["cloud_academic"]
    collist = mydb.list_collection_names()
    res = []
    for str in collist:
        if (str == database):
            mycol = mydb[str]
        else:
            continue
        res = mycol.find({"organizationName": organizationName, "collegeName": collegeName}).distinct('name')
        myclient.close()
        return res


def getPersonInfoByName(database,organizationName,collegeName,personName):
    myclient = pymongo.MongoClient("mongodb://localhost:27017")
    dblist = myclient.list_database_names()
    if "cloud_academic" not in dblist:
        print("数据库不存在！")
        return 0
    mydb = myclient["cloud_academic"]
    collist = mydb.list_collection_names()
    res = {}
    for str in collist:
        if (str == database):
            mycol = mydb[str]
        else:
            continue
        content = mycol.find({"organizationName": organizationName, "collegeName": collegeName, \
            "name": personName}).distinct('content')
        specContent = hanlp_process.getContent(content[0])
        res['content'] = content
        res['specContent'] = specContent
        res['departmentName'] = mycol.find({"organizationName": organizationName, "collegeName": collegeName, \
            "name": personName}).distinct('departmentName')
        res['mainPage'] = mycol.find({"organizationName": organizationName, "collegeName": collegeName, \
            "name": personName}).distinct('mainPage')
        res['match'] = mycol.find({"organizationName": organizationName, "collegeName": collegeName, \
            "name": personName}).distinct('match')
        res['title'] = mycol.find({"organizationName": organizationName, "collegeName": collegeName, \
            "name": personName}).distinct('title')
        res['phone'] = mycol.find({"organizationName": organizationName, "collegeName": collegeName, \
            "name": personName}).distinct('phone')
        res['email'] = mycol.find({"organizationName": organizationName, "collegeName": collegeName, \
            "name": personName}).distinct('email')
        res['website'] = mycol.find({"organizationName": organizationName, "collegeName": collegeName, \
            "name": personName}).distinct('website')
        myclient.close()
        return res


def getUrlByOrganizationNameAndCollegeName(organizationName, collegeName):
    myclient = pymongo.MongoClient("mongodb://localhost:27017")
    dblist = myclient.list_database_names()
    if "cloud_academic" not in dblist:
        print("数据库不存在！")
        return 0
    mydb = myclient["cloud_academic"]
    collist = mydb.list_collection_names()
    for str in collist:
        if (str == 'organization'):
            mycol = mydb[str]
        else:
            continue
        x = mycol.find({"organizationName": organizationName, "collegeName": collegeName})
    myclient.close()
    res = []
    for i in x:
        res.append(i['url'])
    return ','.join(i for i in res)


# getCollegeNameList("江南大学")
# print(getUrlByOrganizationNameAndCollegeName("成都文理学院","文法学院"))

def addUrl(organizationName, collegeName, url):
    myclient = pymongo.MongoClient("mongodb://localhost:27017")
    dblist = myclient.list_database_names()
    data = {"organizationName": organizationName, "collegeName": collegeName, "url": url, "是否采集学院": "false"}
    if "cloud_academic" not in dblist:
        print("数据库不存在！")
        return 0
    mydb = myclient["cloud_academic"]
    collist = mydb.list_collection_names()
    for str in collist:
        if (str == 'organization'):
            mycol = mydb[str]
            mycol.insert_one(data)
        else:
            continue

def updateUrl(organizationName, collegeName, url):
    myclient = pymongo.MongoClient("mongodb://localhost:27017")
    dblist = myclient.list_database_names()
    if "cloud_academic" not in dblist:
        print("数据库不存在！")
        return 0
    mydb = myclient["cloud_academic"]
    collist = mydb.list_collection_names()
    for str in collist:
        if (str == 'organization'):
            mycol = mydb[str]
            mycol.update_one({"organizationName": organizationName,"collegeName": collegeName},{"$set":{"url":url}})
        else:
            continue

def updateScholarById(id,data):
    myclient = pymongo.MongoClient("mongodb://localhost:27017")
    dblist = myclient.list_database_names()
    if "cloud_academic" not in dblist:
        print("数据库不存在！")
        return 0
    mydb = myclient["cloud_academic"]
    collist = mydb.list_collection_names()
    for str in collist:
        if (str == 'scholar_temp'):
            mycol = mydb[str]
            mycol.update_one({"_id": id},
                             {"$set": data})
        else:
            continue