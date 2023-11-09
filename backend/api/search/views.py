from django.shortcuts import render
from util.third_party_api.x_api import XApi
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json

# Create your views here.


class Search(APIView):
    def __init__(self):
        super().__init__()
        self.__x_api = XApi()

    def get(self, request):
        x_res = self.__x_api.search()
        response_data = json.loads(x_res.text)["data"]

        try:
            response_data["user_query"] = request.query
        except:
            pass

        return Response(response_data, status=status.HTTP_200_OK)
