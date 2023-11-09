from django.shortcuts import render
from requests_oauthlib import OAuth1Session
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.settings.local import *
import json

# Create your views here.


class Search(APIView):
    def __init__(self):
        super().__init__()
    
    def get(self, request):
        x = OAuth1Session(X_API_KEY, X_API_KEY_SECRET, X_ACCESS_TOKEN, X_ACCESS_TOKEN_SECRET)
        url = 'https://api.twitter.com/2/users/me'
        res = x.get(url)
        response_data = json.loads(res.text)['data']

        if request.query:
            response_data['user_query'] = request.query

        return Response(response_data, status=status.HTTP_200_OK)