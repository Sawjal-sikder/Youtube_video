# POSTGRESQL DATABASE implementaion
#### Section 1: Install PostgreSQL on Ubuntu
```
sudo apt update
sudo apt install postgresql postgresql-contrib
```

#### Section 2: Create PostgreSQL User & Database
```
sudo -u postgres psql
```

-- Create a new user
```
CREATE USER yourusername WITH PASSWORD 'yourpassword';
```

-- Create a new database
```
CREATE DATABASE yourdbname OWNER yourusername;
```

-- Grant permissions
```
GRANT ALL PRIVILEGES ON DATABASE yourdbname TO yourusername;
```

####  Section 3: Connect Django to PostgreSQL

-- Install psycopg:
```
pip install psycopg2-binary
```

-- Update settings.py for database setup
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'yourdbname',
        'USER': 'yourusername',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

-- Run migrations:
```
python manage.py migrate
```
