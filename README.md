
# Django session for same page redrect
#### 1. view.py
```
    return redirect(request.META.get('HTTP_REFERER', '/'))
```

# Django static & media file setup
#### 1. Settings.py

```
STATIC_URL = 'static/'
MEDIA_URL = 'media/'
STATICFILES_DIRS = [BASE_DIR / 'static', ]
MEDIA_ROOT = BASE_DIR / 'media'
```
#### 2. urls.py
```
from django.conf import settings
from django.conf.urls.static import static


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```



# Django Modal form with widgets
#### 1. form.py

```
# forms.py
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author', 'image', 'details']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the post title'
            }),
            'author': forms.Select(attrs={
                'class': 'form-control'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
            'details': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write the details here...'
            }),
        }
```




# Django url button fix in javascripts
#### 1. Django url button fix in javascripts

```
<button onclick="location.href='{% url 'home' item.id %}'">Go to Home</button>
```


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




