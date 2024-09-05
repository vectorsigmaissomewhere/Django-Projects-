## When you logs in it saves the ip in session using signals 

Here I have only set the logic, implement it in your way 

signals.py
```python
from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User
from django.dispatch import receiver

# When user is logged in it saves the ip address
@receiver(user_logged_in, sender=User)
def login_success(sender, request, user, **kwargs):
    print("----------------------------")
    print("Logged-in Signal.. Run Intro")
    ip = request.META.get('REMOTE_ADDR') 
    print("Client IP:", ip)
    request.session['ip'] = ip
```

TO make this work

apps.py
```python
from django.apps import AppConfig

class BlogConfig(AppConfig):
    name = 'blog' # your name of the application

    def ready(self):
        import blog.signals
```

init.py
```python
default_app_config = 'blog.apps.BlogConfig'
```

views.py
```python
def showip(request):
    if request.user.is_authenticated:
        ip = request.session.get('ip',0)
        return render(request, {'ip': ip})
```
