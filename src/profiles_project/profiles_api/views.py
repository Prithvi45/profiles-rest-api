from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import  serializers

# Create your views here.

class HelloAPIView(APIView):
    """ Test API View  """

    serializer_class = serializers.HelloSerializers
    def get(self, request, format=None):
        """ Returns a list of APIView features"""

        an_apiview =[
        'Uses HTTP methods as function (get, post, patch, put delete)',
        'It is similar to traditional django view',
        'Gives you the most control over your logic ',
        'It is mapped manually to urls'
        ]

        return Response({'message':'Hello!','api_view':an_apiview})

    def post(self, request):
        """ create a hello msg with our name """
        serializer = serializers.HelloSerializers(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message':message, 'name':name})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk=None):
        """ Handles updating an object """

        return Response({'method':'put'})

    def patch(self, request, pk=None):
        """ Patch request, only updates fields provided in the request"""

        return Response({'method':'patch'})

    def delete(self, request, pk=None):
        """ Deletes objects """

        return Response({'method':'delete'})
