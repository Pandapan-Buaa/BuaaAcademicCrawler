from django.shortcuts import render
from BaseApiView.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler
from rest_framework import permissions
from mongo.utils import getAll, getByOrganizationName, getOrganizationNameList, getCollegeNameList, \
    getByOrganizationNameAndCollegeName, getUrlByOrganizationNameAndCollegeName, addUrl, updateUrl
from buaaac import settings
from django.views.decorators.csrf import csrf_exempt
import time
import os
from django.http import HttpResponse
import csv
import pymongo
import codecs


class getAllInfo(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        res = {}
        res["count"] = getAll()
        res["code"] = 20000
        return Response(res)


class getByName(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        res = {}
        organizationName = request.GET['organizationName']
        collegeName = request.GET['collegeName']
        res["total_count"] = getByOrganizationName(organizationName)
        res["count"] = getByOrganizationNameAndCollegeName(organizationName, collegeName)
        res["code"] = 20000
        res["organizationName"] = organizationName
        res["collegeName"] = collegeName
        return Response(res)


class getUrlByName(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        res = {}
        organizationName = request.GET['organizationName']
        collegeName = request.GET['collegeName']
        res["url"] = getUrlByOrganizationNameAndCollegeName(organizationName, collegeName)
        res["code"] = 20000
        res["organizationName"] = organizationName
        res["collegeName"] = collegeName
        return Response(res)

    def post(self, request):
        res = {}
        organizationName = request.GET['organizationName']
        collegeName = request.GET['collegeName']
        url = request.GET['url']
        addUrl(organizationName, collegeName, url)
        res["url"] = url
        res["code"] = 20000
        res["organizationName"] = organizationName
        res["collegeName"] = collegeName
        return Response(res, status=status.HTTP_201_CREATED)

    def put(self, request):
        res = {}
        organizationName = request.GET['organizationName']
        collegeName = request.GET['collegeName']
        url = request.GET['url']
        updateUrl(organizationName, collegeName, url)
        res["url"] = url
        res["code"] = 20000
        res["organizationName"] = organizationName
        res["collegeName"] = collegeName
        return Response(res, status=status.HTTP_201_CREATED)


class getOrganizationName(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        res = {}
        res["data"] = getOrganizationNameList(request.GET['database'])
        res["code"] = 20000
        return Response(res)


class getCollegeName(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        res = {}
        res["data"] = getCollegeNameList(request.GET['database'], request.GET['organizationName'])
        res["code"] = 20000
        return Response(res)


class exportAsCSV(APIView):
    def get(self, request):
        # res = {}

        # res['code'] = 20000
        # response = Response(res,content_type='text/csv')
        response = HttpResponse(content_type='application/octet-stream')
        response['Content-Disposition'] = 'attachment; filename=unruly.csv'

        myclient = pymongo.MongoClient("mongodb://localhost:27017")
        dblist = myclient.list_database_names()
        if "cloud_academic" not in dblist:
            print("数据库不存在！")
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        mydb = myclient["cloud_academic"]
        collist = mydb.list_collection_names()
        for str in collist:
            if (str == 'organization'):
                mycol = mydb[str]
                response.write(codecs.BOM_UTF8)
                writer = csv.writer(response)
                # 先写列名
                # 写第一行，字段名
                fieldList = [
                    "_id",
                    "organizationName",
                    "collegeName",
                    "url",
                    "是否采集学院",
                ]

                writer.writerow(fieldList)
                allRecordRes = mycol.find({"是否采集学院": "false"})
                for record in allRecordRes:
                    # print(f"record = {record}")
                    recordValueLst = []
                    for field in fieldList:
                        if field not in record:
                            recordValueLst.append("None")
                        else:
                            recordValueLst.append(record[field])
                    try:
                        writer.writerow(recordValueLst)
                    except Exception as e:
                        print(f"write csv exception. e = {e}")
            else:
                continue

        return response