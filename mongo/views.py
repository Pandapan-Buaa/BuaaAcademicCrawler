from django.shortcuts import render
from BaseApiView.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler
from rest_framework import permissions
from mongo.utils import getAll, getByOrganizationName, getOrganizationNameList,getCollegeNameList,getByOrganizationNameAndCollegeName,getUrlByOrganizationNameAndCollegeName
from buaaac import settings
from django.views.decorators.csrf import csrf_exempt
import time
import os


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
        res["count"] = getByOrganizationNameAndCollegeName(organizationName,collegeName)
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
        res["url"] = getUrlByOrganizationNameAndCollegeName(organizationName,collegeName)
        res["code"] = 20000
        res["organizationName"] = organizationName
        res["collegeName"] = collegeName
        return Response(res)

class getOrganizationName(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        res = {}
        res["data"] = getOrganizationNameList()
        res["code"] = 20000
        return Response(res)


class getCollegeName(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        res = {}
        res["data"] = getCollegeNameList(request.GET['organizationName'])
        res["code"] = 20000
        return Response(res)