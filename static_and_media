## Static and Media file 

```
from django.views.static import serve
from django.urls import re_path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += [
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
```
