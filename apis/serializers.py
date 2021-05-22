from rest_framework import serializers
from yt_api.models import *

class VideoDataSerializers(serializers.ModelSerializer):
    class Meta:
        model = VideoData
        fields='__all__'
    def create(self,validated_data):
        return VideoData.objects.create(**validated_data)