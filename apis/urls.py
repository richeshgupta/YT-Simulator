from django.contrib import admin
from django.urls import path,include
from .views import VideoDataApiView,VideoSearchApiView
urlpatterns = [
    path('getVideoData/',VideoDataApiView.as_view(),name='get-video'),
    path('getSearch/',VideoSearchApiView.as_view(),name='search'),

]
