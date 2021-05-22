from django.db import models

# Create your models here.

class VideoData(models.Model):
    vid_id = models.CharField(max_length=100,db_index=True)
    title = models.CharField(max_length=100)
    thumbnails = models.URLField(max_length=200)
    description = models.TextField()
    pub_date = models.CharField(max_length=25)
    
    def __str__(self):
        return self.title + " : " + str(self.pub_date)
    