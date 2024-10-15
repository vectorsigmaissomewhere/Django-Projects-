
## Class Based View with login required and staff member required Decorators in Django 

login_required Decorator
```text
login_required(redirect_field='next', login_url=None)
If the user is logged in, execute the view normally. The view code is free to assume 
the user is logged in.
If the user isn't logged in, redirect to settings.LOGIN_URL, passing the current absolute 
path in the query string. Example: /accounts/login/?next=/accounts/profile/
django.contrib.auth.decorators.login_required

Where, 
redirect_field_name - If you would prefer to use  a different name for this parameter, 
login_required() takes an optional redirect_field_name parameter. If you provide a value
to redirect_field_name, you will most likely need to customize your login template as well, 
since the template context variable which stores the redirect path will use the value of 
redirect field_name as its key rather than "next" (the default).

login_url - If you don't specify the login_url parameter, you'll need to ensure that the 
settings.LOGIN_URL and your login view are properly associated.
```

staff_member_required decorator
```text
staff_member_required(redirect_field_name='next', login_url='admin:login')
This decorator is used on the admin views that require authorization. A view decorated 
with this function will having the following behavior.
- If the user is logged in, is a staff member(User.is_staff=True), and 
is active(User.is_active=True), execute the view normally.
- Otherwise, the request will be redirected to the URL specified by the login_url 
parameter, with the originally requested path in a query string variable specified by 
redirect_field_name.
For example: /admin/login/?next=/profile/
```

permission_required Decorator
```text
permission_required(perm, login_ur=None, raise_exception=False)

It's a relatively common task to check whether a user has a particular permission. For that 
reason, Django provides a shortcut for those case: the permission_requireed() decorator.

Just like the has_perm() method, permission names take the form 
"<app label>.<permission codename>"
```

Decorating Class-Based View
```text
Decorating in urls.py or URLconf
The simplest way of decorating class-based views is to decorate the result of the 
as_view() method. The easiest place to do this is in the URLconf where you deploy 
your view:
from django.urls import path
from django.views.generic import TemplateView 
from registration.views.import ProfileTemplateView 
from django.contrib.auth.decorators import login_required 
urlpatterns = [
    path('dashboard/', login_required(TemplateView.as_view(template_name='bash/dash.html')), name='dash'),
    path('profile/', login_required(ProfileTemplateView.as_view(template_name='registration/profile.html')), name='profile'),
    path('blogpost/', permission_required('blog.can_add')(BlogPostView.as_view())),
]
```

method_decorator
```text
The method_decorator decorator transforms a function decorator into a method decorator so 
that is can be used on an instance method.

A methon on a class isn't quite the same as a standalone function, so you can't just apply 
a function decortaor to the method you need to transform it into a method decorator first.

@method_decorator(*args, **kwargs)
```

Decorating in the Class
```text
To decorate every instance of a class-based view, you need to decorate the class 
definition itself. To do this you apply the decorator to the dispatch() method of the 
class.

from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

class ProfileTemplateView(TemplateView):
    template_name = 'registration/profile.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

You can decorate the class instead and pass the name of the method to be decorated as the 
keyword argument name:

@method_decorator(login_required, name='dispatch')
class ProfileTemplateView(TemplateView):
    template_name = 'registration/profile.html'

If you have a set of common decorators used in several places, you can define a list 
or tuple of decorators and use this instead of invoking method_decorator() multiple times.
@method_decorator(never_cache, name='dispatch')
@method_decorator(login_required, name='dispatch')
class ProfileTemplateView(TemplateView):
    template_name = 'registration/profile.html'

decorators = [never_cache, login_required]
@method_decorator(decorators, name='dispatch')
class ProfileTemplateView(TemplateView):
    template_name = 'registration/profile.html'

The decorators will process a request in the order they are passed to the decorator.
In the example, never_cache() will process the request before login_required().
```
