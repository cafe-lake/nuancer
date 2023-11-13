from django.shortcuts import render
from util.third_party_api.x_api import XApi
from util.third_party_api.openai_api import OpenAiApi
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json

# Create your views here.


class Search(APIView):
    def __init__(self):
        super().__init__()
        self.__x_api = XApi()
        self.__openai_api = OpenAiApi()

    def get(self, request):
        # ツイートをまずは検索
        try:
            x_res = self.__x_api.search()
        except:
            return Response([], status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        response_data = json.loads(x_res.text)["data"]

        # 検索結果が相応しいかチェック
        try:
            request.query = "デ・ブライネ　やばい"
            tweet = "デ・ブライネ調子悪いな。ハーランドはやばい。"
            openai_res = self.__openai_api.evaluate(request.query, tweet)
        except:
            return Response([], status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        response_data["user_query"] = request.query
        response_data["is_de_bruyne_yabai"] = openai_res

        return Response(response_data, status=status.HTTP_200_OK)
