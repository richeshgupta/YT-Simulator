from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator
from yt_api.models import *


def SearchResults(request,query):
    """
        Querying DB to match Description or Title
    """
    
    if(request.method=="GET"):
        if(query==None):
            return ErrorPage(request,"No Query Passed")
        query = query.split()
        obj = VideoData()
        res_set = Q()
        for i in query:
            res_set = VideoData.objects.filter(Q(title__icontains = i) | Q(description__icontains = i))
        
        # Pagination
        paginator = Paginator(res_set, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'results':page_obj,
        }
    return render(request,"search_results.html",context)

