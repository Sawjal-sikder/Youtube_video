Getting started
===============

Requirements
------------

* Python (3.9, 3.10, 3.11, 3.12, 3.13)
* Django (4.2, 5.0, 5.1)
* Django REST Framework (3.14, 3.15)

These are the officially supported python and package versions.  Other versions
will probably work.  You're free to modify the tox config and see what is
possible.

Installation
------------

Simple JWT can be installed with pip:

``` 
pip install djangorestframework
pip install djangorestframework-simplejwt
pip install django-filter
```
  

Project Configuration
---------------------

Then, your django project must be configured to use the library.  In
``settings.py``, add
``rest_framework_simplejwt.authentication.JWTAuthentication`` to the list of
authentication classes:


```
 INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework_simplejwt',
    'django_filters',
]

```
and 

```
from datetime import timedelta

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',

    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
}

```

Also, in your root ``urls.py`` file (or any other url config), include routes
for Simple JWT's ``TokenObtainPairView`` and ``TokenRefreshView`` views:

```

  from rest_framework_simplejwt.views import (
      TokenObtainPairView,
      TokenRefreshView,
  )

  urlpatterns = [
      
      path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
      path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
      
  ]
```

