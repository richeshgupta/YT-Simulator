from django.http.response import HttpResponse
from yt_api.yt_requester import youtube_search
from django.shortcuts import render
from yt_api.yt_requester import *
import io
from django.http import HttpResponse
import json
from .app_serializers import VideoDataSerializers
from .models import *
from django.core.paginator import Paginator
import json
from search.views import SearchResults
import datetime


def process_data(json_dict):
    items = json_dict["items"]
    video_id=[]
    title=[]
    description = []
    pub_date = []
    thumbnails = []

    
    for i in range(len(items)):
        
        video_id = items[i]["id"]["videoId"]

        # If video is already in DB, we won't save it again.
        isUnique = not (VideoData.objects.filter(vid_id=video_id).exists())
        if isUnique==True:
            snippet = items[i]["snippet"]
            title=snippet["title"]
            description = snippet["description"]
            pub_date = snippet['publishedAt']
            thumbnails = snippet["thumbnails"]["medium"]['url']
            obj = VideoData(title=title,vid_id=video_id,pub_date = pub_date,description=description,thumbnails=thumbnails)
            obj.save()

    
    return [title,thumbnails,description,pub_date,video_id]


  

def IndexView(request):
    if(request.method=="GET"):
        search_query = request.GET.get('q')
        if(search_query!=None and len(search_query)>0):
            return SearchResults(request,search_query)
        try:
            yt_data = youtube_search()    
            print(yt_data)
            processed_data = process_data(yt_data)
            
        except Exception as e:
            # This block Can be used to swap API KEYS
            print("ERROR : ",str(e))
            print("API LIMIT EXHAUSTED!")
        
        vid_objs = VideoData.objects.all().order_by('-id')
        paginator = Paginator(vid_objs, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        context = {
            'page_obj':page_obj,
            'videos':page_obj,
        }
        return render(request,"index.html",context)

def ErrorPage(request,message):
    return render(request,"error.html",{'msg':message})




