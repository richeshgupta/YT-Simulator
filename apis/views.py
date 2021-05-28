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
from yt_api.yt_requester import youtube_search
from yt_api.views import process_data

class VideoDataApiView(APIView):
    def get(self, request, *args, **kwargs):
        '''
        List all the VideoData items in a DB
        '''
        
        try:
            yt_data = youtube_search()    
            processed_data = process_data(yt_data)
        except Exception as e:
            print(str(e))
        data = VideoData.objects.all().order_by('id')
        
        serializer = VideoDataSerializers(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class VideoSearchApiView(APIView):
    def get(self, request, *args, **kwargs):
        '''
        List all the VideoData items that matches the query in a DB
        '''
        
        
        query = request.query_params.get('query',None)

        if(query==None or len(query)<1):
            
            serializer = VideoDataSerializers([], many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            query = query.split() 
            obj = VideoData()
            res_set = Q()
            for i in query:
                res_set = VideoData.objects.filter(Q(title__icontains = i) | Q(description__icontains = i))

            serializer = VideoDataSerializers(res_set, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)