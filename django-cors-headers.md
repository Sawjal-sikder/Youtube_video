# Setup
Install from pip:

```
python -m pip install django-cors-headers
```

and then add it to your installed apps:
```
INSTALLED_APPS = [
    "corsheaders",
]
```

You will also need to add a middleware class to listen in on responses:
```
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
]
```

Configure the middleware’s behaviour in your Django settings. You must set at least one of three following settings:

```
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOWS_CREDENTIALS = True
```
