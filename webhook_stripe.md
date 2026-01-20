Stripe Dashboard to proceed:
STRIPE_PUBLISHABLE_KEY
STRIPE_SECRET_KEY
STRIPE_WEBHOOK_SECRET
How to create and share the STRIPE_WEBHOOK_SECRET
Please follow the steps below:
Log in to your Stripe Dashboard
Click on Developers
Navigate to Webhooks
Click Add destination
In the Destination URL, enter:
https://yourdomain/api/payment/webhook/
Select the following events:
```
checkout.session.completed
```
```
customer.created
```
```
customer.updated
```
```
customer.subscription.created
```
```
customer.subscription.deleted
```
```
customer.subscription.updated
```
```
customer.subscription.trial_will_end
```
```
invoice.paid
```
```
invoice.payment_failed
```
```
invoice.payment_succeeded
```

Save the webhook configuration
After saving, copy the Signing Secret — this is your STRIPE_WEBHOOK_SECRET
Share the STRIPE_WEBHOOK_SECRET securely with us
If you encounter any issues while setting this up, please let us know and we’ll be happy to assist.

 
