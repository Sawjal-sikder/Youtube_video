Youtube Video 
Install embed Video
pip install django-embed-video
&
INSTALLED_APPS = [
   'embed_video',
]
Model.py
from django.db import models
from embed_video.fields import EmbedVideoField
# Create your models here.
class videos(models.Model):
   title = models.CharField(max_length=100)
   addDate = models.DateTimeField(auto_now_add=True)
   url = EmbedVideoField()


   def __str__(self):
       return str(self.title)


   class Meta:
       ordering = ['-addDate']


Admin.py
from django.contrib import admin
from .models import videos
# Register your models here.
admin.site.register(videos)


views.py
from django.shortcuts import render
from .models import videos
# Create your views here.
def home(request):
   video = videos.objects.all()
   return render(request,'home.html',{'videos' : video})


html
{% extends  'base.html' %}
{% load embed_video_tags %}


{% block title %} Home Page {% endblock %}
{% block body %}
{% for item in videos %}
{% video item.url '426x240' %}
{{ item.title }}
{% endfor  %}
{% endblock %}




