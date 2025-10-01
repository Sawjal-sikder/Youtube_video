shell use for modal data
```bash
python manage.py shell
```

show json data
```bash
import json
from django.forms.models import model_to_dict
from payment.models import Plan
plans = Plan.objects.all()
for plan in plans:
  print(json.dumps(model_to_dict(plan), indent=2))
```
show json data for serializers
```bash
from django.core import serializers
from django.contrib.auth import get_user_model

User = get_user_model()
users = User.objects.all()

print(serializers.serialize("json", users, indent=2))
```
