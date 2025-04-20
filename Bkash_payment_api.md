# Payment for bkash
### Install Required Packages
```
Install Required Packages
```

### Configure Django Settings
```
BKASH_CONFIG = {
    'BASE_URL': 'https://checkout.sandbox.bka.sh/v1.2.0-beta',
    'APP_KEY': 'your_app_key',
    'APP_SECRET': 'your_app_secret',
    'USERNAME': 'your_username',
    'PASSWORD': 'your_password',
    'GRANT_TOKEN_URL': 'https://checkout.sandbox.bka.sh/v1.2.0-beta/checkout/token/grant',
}
```

### Step:3 Token Generation
```
import requests
from django.conf import settings

def get_bkash_token():
    url = settings.BKASH_CONFIG['GRANT_TOKEN_URL']
    headers = {
        'username': settings.BKASH_CONFIG['USERNAME'],
        'password': settings.BKASH_CONFIG['PASSWORD']
    }
    data = {
        'app_key': settings.BKASH_CONFIG['APP_KEY'],
        'app_secret': settings.BKASH_CONFIG['APP_SECRET'],
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()  # Contains 'id_token' to use in future API calls
```

### Step:4 Create Payment Request
```
def create_bkash_payment(token, amount, invoice_number):
    url = f"{settings.BKASH_CONFIG['BASE_URL']}/checkout/payment/create"
    headers = {
        "Authorization": token,
        "X-APP-Key": settings.BKASH_CONFIG['APP_KEY'],
        "Content-Type": "application/json"
    }
    body = {
        "mode": "0011",
        "payerReference": "your_user_id_or_phone",
        "callbackURL": "https://yourdomain.com/bkash/callback/",
        "amount": str(amount),
        "currency": "BDT",
        "intent": "sale",
        "merchantInvoiceNumber": invoice_number
    }
    response = requests.post(url, headers=headers, json=body)
    return response.json()
```

### Step:5 Execute Payment After User Authorizes
```
def execute_bkash_payment(token, payment_id):
    url = f"{settings.BKASH_CONFIG['BASE_URL']}/checkout/payment/execute/{payment_id}"
    headers = {
        "Authorization": token,
        "X-APP-Key": settings.BKASH_CONFIG['APP_KEY']
    }
    response = requests.post(url, headers=headers)
    return response.json()
```


### Step:6 Callback or Redirect View
```
from django.http import JsonResponse

def bkash_callback(request):
    # Handle success or failure
    return JsonResponse({'message': 'Callback received'})
```


### Step:7 Check Payment Status
```
def query_payment(token, payment_id):
    url = f"{settings.BKASH_CONFIG['BASE_URL']}/checkout/payment/query/{payment_id}"
    headers = {
        "Authorization": token,
        "X-APP-Key": settings.BKASH_CONFIG['APP_KEY']
    }
    response = requests.get(url, headers=headers)
    return response.json()
```
