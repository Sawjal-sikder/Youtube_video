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
