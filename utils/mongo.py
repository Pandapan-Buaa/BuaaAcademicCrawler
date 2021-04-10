import pymongo
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
        print(res)
        return res
        # for organization in x:
        #     y = mycol.find({'organizationName':organization}).distinct('collegeName')
        #     z = []
        #     for college in y:
        #         z.append(college)
        #     dict[organization] = z
# def updateScholarById(id,data):
#     myclient = pymongo.MongoClient("mongodb://localhost:27017")
#     dblist = myclient.list_database_names()
#     if "cloud_academic" not in dblist:
#         print("数据库不存在！")
#         return 0
#     mydb = myclient["cloud_academic"]
#     collist = mydb.list_collection_names()
#     for str in collist:
#         if (str == 'scholar_temp'):
#             mycol = mydb[str]
#             mycol.update_one({"_id": id},
#                              {"$set": data})
#         else:
#             continue
# # getOrganizationName()
# id = "645bfcebb7274352acb4e6f9041b3e2f"
# data = {
#     "organizationName": "江南大学",
#     "collegeName": "设计学院",
#     "name": "谢玉梅",
#     "title": "教授",
#     "email": "xieym66@jiangnan.edu.cn",
#     "phone": "null",
# }
# updateScholarById(id,data)