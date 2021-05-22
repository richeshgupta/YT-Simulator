
from django.contrib import admin
from django.urls import path
from .views import  SearchResults


urlpatterns = [
    path('search?q=<str:query>/', SearchResults,name='search-res'),
]
