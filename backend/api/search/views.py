from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class Search(APIView):
    def __init__(self):
        super().__init__()
    
    def get(self, request):
        response_data = {
            'id': 1,
            'content': 'Hello, world.'
        }
        return Response(response_data, status=status.HTTP_200_OK)