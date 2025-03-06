# dotenv for python django secrect key
#### install environment
```
pip install python-dotenv
```
#### Create a .env File and setup secret key

```
# Email Settings
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
```
#### Configure settings.py for dotenv
```
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Get email settings from environment variables
EMAIL_BACKEND = os.getenv("EMAIL_BACKEND")
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = int(os.getenv("EMAIL_PORT"))  # Convert to integer
EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS") == "True"  # Convert to boolean
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
```
