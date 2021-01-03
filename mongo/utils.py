import pymongo
def getAll():
    myclient = pymongo.MongoClient("mongodb://localhost:27017")
    dblist = myclient.list_database_names()
    if "cloud_academic" not in dblist:
        print("数据库不存在！")
        return 0
    mydb = myclient["cloud_academic"]
    collist = mydb. list_collection_names()
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

def getByName(name):
    myclient = pymongo.MongoClient("mongodb://localhost:27017")
    dblist = myclient.list_database_names()
    if "cloud_academic" not in dblist:
        print("数据库不存在！")
        return 0
    mydb = myclient["cloud_academic"]
    collist = mydb. list_collection_names()
    count = 0
    for str in collist:
        if (str == 'scholar_temp'):
            mycol = mydb[str]
        else:
            continue
        x = mycol.find({"organizationName":name})
        count += x.count()
    myclient.close()
    return count

def getOrganizationName():
    myclient = pymongo.MongoClient("mongodb://localhost:27017")
    dblist = myclient.list_database_names()
    if "cloud_academic" not in dblist:
        print("数据库不存在！")
        return 0
    mydb = myclient["cloud_academic"]
    collist = mydb. list_collection_names()
    res = []
    for str in collist:
        if(str == 'scholar_temp'):
            mycol = mydb[str]
        else:
            continue
        myclient.close()
        res = mycol.distinct('organizationName')
        # print(res)
        return res
        # for organization in x:
        #     y = mycol.find({'organizationName':organization}).distinct('collegeName')
        #     z = []
        #     for college in y:
        #         z.append(college)
        #     dict[organization] = z


