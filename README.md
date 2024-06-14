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
       ordering = ['-addDate'```
