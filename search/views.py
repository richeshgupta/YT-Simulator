from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator
from yt_api.models import *

def Search(request):
    return render(request,"search_bar.html",{})

def SearchResults(request,query=None):
    """
        Querying DB to match Description or Title
    """
    
    query = query.split()
    obj = VideoData()
    res_set = Q()
    for i in query:
        res_set = VideoData.objects.filter(Q(title__icontains = i) or Q(description__icontains = i))
    
    # Pagination
    paginator = Paginator(res_set, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'results':page_obj,
    }
    return render(request,"search_results.html",context)

