
from django.shortcuts import render
from BaseApiView.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler
from rest_framework import permissions
from mongo.utils import get_all,get_by_name

class GetAllInfo(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        res = {}
        res["count"]=get_all()
        res["code"] = 20000
        return Response(res)


class GetByName(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        res = {}
        name = request.GET['name']
        res["count"]= get_by_name(name)
        res["code"] = 20000
        res["name"] = name
        return Response(res)