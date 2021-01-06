from django.shortcuts import render
from BaseApiView.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler
from rest_framework import permissions
from mongo.utils import getAll, getByName, getOrganizationName

from buaaac import settings
from django.views.decorators.csrf import csrf_exempt
import time
import os


class GetAllInfo(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        res = {}
        res["count"] = getAll()
        res["code"] = 20000
        return Response(res)


class GetByName(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        res = {}
        name = request.GET['name']
        res["count"] = getByName(name)
        res["code"] = 20000
        res["name"] = name
        return Response(res)


class GetOrganizationName(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        res = {}
        res["data"] = getOrganizationName()
        res["code"] = 20000
        return Response(res)


class XpathFileList(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def get(self,request):
        res = []
        for root, dirs, files in os.walk(settings.MEDIA_ROOT):
            print(files)  # 当前路径下所有非目录子文件
            res = files
        return Response(res,status=status.HTTP_200_OK)

    @csrf_exempt
    def post(self, request):
        file = request.FILES['file']
        print(settings.MEDIA_ROOT)
        save_path = "%s\\xpath\\%s" % (settings.MEDIA_ROOT, str(time.time()) + file.name,)
        print(save_path)
        with open(save_path, "wb") as f:
            for content in file.chunks():
                f.write(content)
        f.close()
        return Response(status=status.HTTP_200_OK)