import pymongo
import time
import csv
# from buaaac import settings
from mongo import hanlp_process
import requests
from functools import cmp_to_key
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


def getPersonInfoByName(database, organizationName, collegeName, personName):
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
        try:
            pos_time_match_list = hanlp_process.getContent(content[0])
            specContent = pos_time_match_list[0]
            pkuStdContent = pos_time_match_list[1]
            pkuPosContent = pos_time_match_list[2]
            res['code'] = 20000
            res['content'] = [simplifyContent(content[0])]
            # simplifyContent(content[0])
            # print(content)
            res['specContent'] = specContent
            res['pkuPosContent'] = pkuPosContent
            res['pkuTimePosContent'] = pkuStdContent
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
        except Exception:
            res['code'] = 404
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

#
def getPersonNameListByOrg(database, organizationName):
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
        res = mycol.find({"organizationName": organizationName}).distinct('name')
        myclient.close()
        return res

def getZhituInfoByAPI(scholarName, orgName):
    apiUrl = "https://zhitulist.com/academic/api/v1/scholars/getScholarByName"
    params = {
        "scholarName": scholarName,
        "orgName": orgName
    }
    res = requests.get(apiUrl, params=params).json()
    scholarId = res.get("data").get("content")[0].get('scholarId')

    return [res.get("data"), scholarId]

def getZhituOrgInfoByAPI(orgName, fieldId, num, database="scholar_temp"):
    personNameList = getPersonNameListByOrg(database, orgName)
    scholarId = getZhituInfoByAPI(personNameList[0], orgName)[1]
    scholarInfoApi = "https://zhitulist.com/academic/api/v1/scholars/" + str(scholarId)
    scholarInfoInApi = requests.get(scholarInfoApi).json().get("data")
    orgId = scholarInfoInApi.get("orgId")
    orgInfoApi = "https://zhitulist.com/academic/api/v1/rank/top-talents-by-orgId"
    if num == 'all':
        num = 1000
        page = 0
        orgData = []
        while True:
            org_params = {
                "fieldId": fieldId,
                "num": num,
                "page": page,
                "orgId": orgId
            }
            zhituOrgInfoApiContent = requests.get(orgInfoApi, params=org_params).json()
            temp = zhituOrgInfoApiContent.get("data")
            if temp == []:
                break
            for item in temp:
                orgData.append(item)
            page = page + 1
    else:
        page = 0
        org_params = {
            "fieldId": fieldId,
            "num": num,
            "page": page,
            "orgId": orgId
        }
        zhituOrgInfoApiContent = requests.get(orgInfoApi, params=org_params).json()
        orgData = zhituOrgInfoApiContent.get("data")
    fields_cnt_dict = {}
    fields_cnt_list = []
    fields_list = []
    paperCount_list = []
    projectCount_list = []
    patentCount_list = []
    innovationIndex_list = []
    for scholarData in orgData:
        scholarId = scholarData.get("id")
        scholarName = scholarData.get("name")
        paperCount_list.append([scholarName, scholarData.get("paperCount")])
        projectCount_list.append([scholarName, scholarData.get("projectCount")])
        patentCount_list.append([scholarName, scholarData.get("patentCount")])
        scholarInfoApi = "https://zhitulist.com/academic/api/v1/scholars/" + str(scholarId)
        scholarInfoInApi = requests.get(scholarInfoApi).json().get("data")
        innovationIndex_list.append([scholarName, scholarInfoInApi.get("innovationIndex")])
        fields = scholarInfoInApi.get("fields")
        for field in fields:
            fieldId = field.get("fieldId")
            fieldName = field.get("fieldName")
            if fieldName not in fields_cnt_dict.keys():
                fields_list.append([fieldName, fieldId])
                fields_cnt_dict[fieldName] = 0
            fields_cnt_dict[fieldName] = fields_cnt_dict[fieldName] + 1
    # get cnt
    for item in fields_cnt_dict.items():
        fields_cnt_list.append({'name': item[0], 'weight': item[1]})
    fields_cnt_list.sort(key=cmp_to_key(lambda x, y: y['weight'] - x['weight']))
    paperCount_list.sort(key=cmp_to_key(lambda x, y: y[1] - x[1]))
    projectCount_list.sort(key=cmp_to_key(lambda x, y: y[1] - x[1]))
    patentCount_list.sort(key=cmp_to_key(lambda x, y: y[1] - x[1]))
    innovationIndex_list.sort(key=cmp_to_key(lambda x, y: y[1] - x[1]))

    return {'fields': fields_list, 'word_cloud': fields_cnt_list, 'paperCount_list': paperCount_list[:10],
            'projectCount_list': projectCount_list[:10], 'patentCount_list': patentCount_list[:10],
            'innovationIndex_list': innovationIndex_list[:10]}
#
def getPersonNameListByOrg(database, organizationName):
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
        res = mycol.find({"organizationName": organizationName}).distinct('name')
        myclient.close()
        return res

def getPersonListInfo(scholarList, orgName):
    paperCountList = []
    projectCountList = []
    for scholarName in scholarList:
        scholarInfo = getZhituInfoByAPI(scholarName, orgName)
        if len(scholarInfo["content"]) > 0:
            paperCountList.append([scholarInfo["content"][0]["name"], scholarInfo["content"][0]["paperCount"]])
            projectCountList.append([scholarInfo["content"][0]["name"], scholarInfo["content"][0]["projectCount"]])
    paperCountList.sort(key=cmp_to_key(lambda x, y: y[1] - x[1]))
    projectCountList.sort(key=cmp_to_key(lambda x, y: y[1] - x[1]))

    return {'paperCountList': paperCountList[:10], 'projectCountList': projectCountList[:10]}

def getPersonNameListByCollege(database, organizationName, collegeName):
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

def getZhituRelationByAPI(scholarId):
    relationGraphApi = "https://zhitulist.com/academic/api/v1/scholars/" + str(scholarId) + "/co-authors"
    print("relationGraphApi : ", relationGraphApi)
    res = requests.get(relationGraphApi).json()
    links = res.get('data').get('links')
    link_list = []
    for link_dict in links:
        link = [link_dict.get('source'), link_dict.get('target')]
        link_list.append(link)
    return [res.get("data"), link_list]

def simplifyContent(content):
    conBeginStrs = ['个人经历', '简历']
    paperBeginStrs = ['论文', '论著']
    newContent = content
    for str in conBeginStrs:
        if str in content:
            # print(content.split(str))
            newContent = content.split(str)[1]
            break
    for str in paperBeginStrs:
        if str in newContent:
            newContent = newContent.split(str)[0]
    newContent = newContent.strip().strip("：").strip(":").strip()
    print(newContent)
    return newContent


def getMultiIdScholarList():
    myclient = pymongo.MongoClient("mongodb://localhost:27017")
    dblist = myclient.list_database_names()
    if "cloud_academic" not in dblist:
        print("数据库不存在！")
        return 0
    mydb = myclient["cloud_academic"]
    collist = mydb.list_collection_names()
    count = 0
    for str in collist:
        if (str == 'scholar_multiid'):
            mycol = mydb[str]
        else:
            continue
        x = list(mycol.find())
    myclient.close()
    return x
