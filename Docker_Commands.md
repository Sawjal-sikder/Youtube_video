## 🔹 Docker General Commands
##### Build image:

```
docker build -t my_django_app .
```

##### Run a container:

```
docker run -it -p 8000:8000 my_django_app
```

##### List running containers:

```
docker ps
```

##### Stop a container:

```
docker stop <container_id>
```

##### Remove stopped containers:

```
docker rm <container_id>
```

##### List images:

```
docker images
```

##### Remove an image:

```
docker rmi <image_id>
```
#🔹 Docker Compose Commands

##### Build all services:
```
docker-compose build
```

##### Start all services:
```
docker-compose up
```

##### Start in background (detached):
```
docker-compose up -d
```

##### Stop services:
```
docker-compose down
```

##### Restart services:
```
docker-compose restart
```

##### See logs (real-time):
```
docker-compose logs -f
```

##### Rebuild + run fresh:
```
docker-compose up --build
```

# 🔹 Django inside Docker

##### Run Django commands inside the container:

```
# Start a new project:
docker-compose run web django-admin startproject myproject .

# creating a new Django app:
docker-compose run web python manage.py startapp myapp

# Migrations:
docker-compose run web python manage.py makemigrations
docker-compose run web python manage.py migrate

# create super user:
docker-compose run web python manage.py createsuperuser

# run shall:
docker-compose run web python manage.py shell

# Collect static files:
docker-compose run web python manage.py collectstatic --noinput
```
