## Function Based View with login_required and staff_member_required Decorators in Django

login_requied Decorator
```text
login_required(redirect_field_name='next', login_url=None)
If the user is logged in, execute the view normally. The view code is free to assume the 
user is logged in.
If the user isn't logged in, redirect to settings.LOGIN_URL, passing the current absolute
path in the query setring. Example: /accounts/login/?next=accounts/profile/
django.contrib.auth.decorators.login_required

Where, 
redirect_field_name - If you would prefer to use a different name for this parameter, 
login_required() takes and optional redirect_field_name parameter. If you provide a 
value to redirect_field_name, you will most likely need to customize your login 
template as well, since the template context variable which stores the redirect path
will use the value of redirect field_name as its key rather than "next" (the default).

login_url - If you don't specify the login_url parameter, you'll need to ensure that
the settings.LOGIN_URL and your login view are properly associated.

The settings.LOGIN_URL also accepts view function names and named URL patterns. This
allows you to freely remap your login view within your URL conf without having to 
update the setting.

Example:
from django.contrib.auth.decorators import login_required
@Login_required
def profile(request):
    return render(request, 'registration/profile.html')
```

staff_member_required decorator
```text
staff_member_required(redirect_field_name='next', login_url='admin:login')
This decorator is used on the admin views that require authorization. A view decorated
with this function will having the following behavior:
- If the user is logged in, is a staff member(User.is_staff=True), 
and is active(User.is_active=True), execute the view normally.
- Otherwise, the request will be redirected to the URL specified by the login_url 
parameter, with the originally requested path in a query string variable specified 
by redirect_field_name.
For example: admin/login/?next=/profile/

Example:-
from django.contrib.admin.views.decorators import staff_member_required
@staff_member_required
def profile(request):
    return render(request, 'registration/profile.html')
```

permission_required Decorator
```text
permission_requied(perm, login_url=None, raise_exception=False)
It's a relatively common task to check whether a user has a particular permission. For that
reason, Django provides a shortcut for that case: the permission_required() decorator.

Just liek the has_perm() method, permission names take the form 
"<app label>.<permission codename>"
Example:-
from django.contrib.auth.decorators import permission_required
@permission_required('blog.can_add')
def profile(request):
    return render(request, 'registration/profile.html')
```


also check jitem 11 for rest of the code

views.py
```python
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required 
# Create your views here.
@login_required
def profile(request):
    return render(request, 'registration/profile.html')

@staff_member_required
def about(request):
    return render(request, 'registration/about.html')
```

Where to find the full code 
```text
check decoratorauthentication
```

What to learn here
```text
how decorator can help unauthorized user to not do unauthorized things in the website
with the help of @login_required and @staff_member_required decorators 
```
