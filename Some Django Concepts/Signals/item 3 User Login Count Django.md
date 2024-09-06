User Login Count Django 

settings.py
```python
CACHES = {
    'default':{
        'BACKEND':'django.core.cache.backends.db.DatabaseCache',
        'LOCATION':'blog_cache',
        }
    }
```

command to hit
```text
first migrate your database
python manage.py createcachetable
```

signals.py
```python
from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.core.cache import cache

@receiver(user_logged_in, sender = User)
def login_success(sender, request, user, **kwargs):
    ct = cache.get('count', 0, version = user.pk) # pk for uniqueness
    newcount = ct + 1
    cache.set('count', newcount, 60*60*24, version=user.pk) # cache stored for one day
    print(user.pk)
```

views.py
```python
from django.core.cache import cache

def home(request):
    ct = cache.get('count', version=user.pk)
    return render(request, 'home.html', {'count': ct})
```
