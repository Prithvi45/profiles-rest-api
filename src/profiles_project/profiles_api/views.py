from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloAPIView(APIView):
    """ Test API View  """

    def get(self, request, format=None):
        """ Returns a list of APIView features"""

        an_apiview =[
        'Uses HTTP methods as function (get, post, patch, put delete)',
        'It is similar to traditional django view',
        'Gives you the most control over your logic ',
        'It is mapped manually to urls'
        ]

        return Response({'message':'Hello!','api_view':an_apiview})
