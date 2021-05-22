from django.shortcuts import render
from django.db.models import Q
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .serializers import VideoDataSerializers
from yt_api.models import *
from functools import reduce
import operator


class VideoDataApiView(APIView):
    def get(self, request, *args, **kwargs):
        '''
        List all the VideoData items in a DB
        '''
        
        data = VideoData.objects.all().order_by('id')
        print("data : ",type(data))
        serializer = VideoDataSerializers(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class VideoSearchApiView(APIView):
    def get(self, request, *args, **kwargs):
        '''
        List all the VideoData items that matches the query in a DB
        '''
        
        
        query = request.query_params.get('query',None)


        print("Query : ",query)
        if(len(query)<1):
            data = VideoData.objects.all().order_by('id')
            print("data : ",type(data))
            serializer = VideoDataSerializers(data, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            query = query.split() 
            obj = VideoData()
            res_set = Q()
            for i in query:
                res_set = VideoData.objects.filter(Q(title__icontains = i) | Q(description__icontains = i))
            print("search : ",type(res_set))
            
            # res_set = VideoData.objects.filter(reduce(operator.or_, res_set))
            serializer = VideoDataSerializers(res_set, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)