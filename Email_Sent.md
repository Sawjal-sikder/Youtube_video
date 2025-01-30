# Sent Email settup in django
#### Email account setup
App Passwords:

1. Go to Google Account Security
2. Scroll down to "How you sign in to Google"
3. Enable 2-Step Verification (if not already enabled)
4. After enabling 2-Step Verification, go to App Passwords
5. Create a new App Password, select Mail as the app and Other (Custom name) for the device
6. Copy the generated password and save it somewhere safe

#### Configure Django Settings.py

```
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "your-email@gmail.com"
EMAIL_HOST_PASSWORD = "zzgk tuls nhzg tgoe"  # Use the App Password generated from Google
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
```
#### Configure Django views.py
```
from django.core.mail import send_mail

send_mail(
    subject="Test Email from Django",
    message="This is a test email sent from Django using Gmail SMTP.",
    from_email="your-email@gmail.com",
    recipient_list=["recipient@example.com"],
    fail_silently=False,
)
```
