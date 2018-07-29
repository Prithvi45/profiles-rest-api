from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import  serializers

#Viewsets
from rest_framework import viewsets
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


class HelloViewSet(viewsets.ViewSet):
    """ Test API Viewset """

    serializer_class = serializers.HelloSerializers
    def list(self, request):
        """ Return a Hello Message """

        a_viewset =[
        'Uses actions (list, create, retrieve, update, partial update)',
        'Automatically maps to URLs using Routers ',
        'Provides more functionality with less code '
        ]

        return Response({'message':'Hello ! i am viewset','a_viewset':a_viewset})

    def create(self, request):
        """ create a new hello message """
        serializer = serializers.HelloSerializers(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}, this a CreateView in HelloViewSet'.format(name)
            return Response({'message':message, 'name':name})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, pk=None):
        """ Handles getting an objects """

        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        """ Updates an object """

        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):
        """ Handles updating part of object """

        return Response({'http_method':'PATCH'})

    def destroy(self, request, pk=None):
        """ Deletes object """

        return Response({'http_method':'DELETE'})
