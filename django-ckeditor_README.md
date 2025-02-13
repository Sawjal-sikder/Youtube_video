## To set up django-ckeditor in your Django project, follow these steps:

#### Step 1. Install django-ckeditor
```
pip install django-ckeditor
```

#### Step 2. Add 'ckeditor' to Installed Apps
```
INSTALLED_APPS = [
    # Other apps
    'ckeditor',
    'ckeditor_uploader',  # Optional (for image uploads)
]
```

#### Step 3. Configure CKEditor in settings.py
```
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',  # Options: 'basic', 'full', 'custom'
        'height': 300,
        'width': '100%',
        'extraPlugins': ','.join([
            'codesnippet',  # Enables code snippet plugin
            'uploadimage',  # Enables image upload support
        ]),
    }
}
```

#### If using image upload, set up media storage:
```
CKEDITOR_UPLOAD_PATH = "uploads/"
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

#### Step 4. Add URL Configurations
```
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    # Other URLs
    path('ckeditor/', include('ckeditor_uploader.urls')),  # Required for image upload
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

#### Step 5. Add CKEditor to Your Model
```
from django.db import models
from ckeditor.fields import RichTextField

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()  # CKEditor field
    content = RichTextUploadingField()  # Allows image uploads

    def __str__(self):
        return self.title
```

#### Step 7. Add CKEditor in Forms (Optional)

```
from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = BlogPost
        fields = '__all__'
```
