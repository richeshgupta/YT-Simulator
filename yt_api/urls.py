
from django.contrib import admin
from django.urls import path
from .views import IndexView


urlpatterns = [
    path('', IndexView,name='yt-api'),
]
