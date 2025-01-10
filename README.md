# Youtube Video 
#### 1. Install embed Video

```
pip install django-embed-video
```
###### Installed App
```
INSTALLED_APPS = [
   'embed_video',
]
```

#### 2. models.py
```
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
       ordering = ['-addDate'
```

#### 3. admin.py

```
from django.contrib import admin
from .models import videos
# Register your models here.
admin.site.register(videos)
```
#### 4. views.py

```
from django.shortcuts import render
from .models import videos
# Create your views here.
def home(request):
   video = videos.objects.all()
   return render(request,'home.html',{'videos' : video})
```
#### 5. Display video html file

```
{% extends  'base.html' %}
{% load embed_video_tags %}


{% block title %} Home Page {% endblock %}
{% block body %}
{% for item in videos %}
{% video item.url '426x240' %}
{{ item.title }}
{% endfor  %}
{% endblock %}
```




# Django url button fix in javascripts
#### 1. Django url button fix in javascripts

```
<button onclick="location.href='{% url 'home' item.id %}'">Go to Home</button>
```
