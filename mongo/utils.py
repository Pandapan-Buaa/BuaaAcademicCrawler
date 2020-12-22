import pymongo
def get_all():
    myclient = pymongo.MongoClient("mongodb://localhost:27017")
    dblist = myclient.list_database_names()
    if "cloud_academic" not in dblist:
        print("数据库不存在！")
        return 0
    mydb = myclient["cloud_academic"]
    collist = mydb. list_collection_names()
    count = 0
    for str in collist:
        mycol = mydb[str]
        x = mycol.find()
        count += x.count()
    myclient.close()
    return count
def get_by_name(name):
    myclient = pymongo.MongoClient("mongodb://localhost:27017")
    dblist = myclient.list_database_names()
    if "cloud_academic" not in dblist:
        print("数据库不存在！")
        return 0
    mydb = myclient["cloud_academic"]
    collist = mydb. list_collection_names()
    count = 0
    for str in collist:
        mycol = mydb[str]
        x = mycol.find({"organizationName":name})
        count += x.count()
    myclient.close()
    return count