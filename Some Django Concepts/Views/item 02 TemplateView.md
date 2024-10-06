
TemplateView
```text
django.views.generic.base.TemplateView

It renders a given template, with the context containing parameters captured in the URL.
This views inherits methods and attributes from the following view:
- django.views.generic.base.TemplateResponseMixin
- django.views.generic.base.ContextMixin
- django.views.generic.base.View

class TemplateView(TemplateResponseMixin, ContextMixin, View):
```

TemplateResponseMixin
```text
It provides a mechanism to construct a TemplateResponse, given suitable context, The template to 
use is configurable and can be further customized by subclass.

Attributes:- 
template_name - The full name of a template to use as defined by a string. Not defining a 
template_name will raise a django.core.exceptions.ImproperlyConfigured exception.

template_engine - The NAME of a template engine to use for loading the template. 
template_engine is passed as the using keyword argument to response_class. Default is None, 
which tell Django to search for the template in all configured engines.

response_class - The response class to be returned by render_to_response method. Default is 
TemplateResponse. The template and context of TemplateResponse instances can be altered later
(e.g. in template response middleware).
If you need custom template loading or custom context object instantiation, create a 
TemplateResponse subclass and assign it to response_class.

content_type - The content type to use for the response.content_type is passed as a keyword
argument to response_class. Default is None - meaning that Django uses 'text/html'.

Methods:- 
render_to_response(context, **response_kwargs) - It returns a self.response_class instance.
If any keyword arguments are provided, they will be passed to the constructor of the response
class.

Calls get_template_names() to obtain the list of template names that will be searched looking
for an existent template.

get_template_names() - It returns a list of template names to search for when rendering the template The first template that is found will be used.
If template_name is specified, the default implementation will return a list containing 
template_name(if it is specified).

A default context mixin that passes the keyword arguments received by get_context_data() as the 
template context.
Attribute:- 
extra_context - A dictionary to include in the context. This is a convenient way of specifying 
some context in as_view().

Method:- 
get_context_data(**kwargs) - It returns a dictionary representing the template context. The 
keyword arguments provided will make up the returned context.
```

Example
```python
# views.py
from django.views.generic.base import TemplateView
class HomeView(TemplateView):
  template_name = 'school/home.html'

# urls.py
from school import views
urlpatterns = [
  path('home/', views.HomeView.as_view(), name='home'),
]
```

TemplateView With Context
```python
# views.py
from django.views.generic.base import TemplateView
class HomeView(TemplateView):
  template_name = 'school/home.html'

  def get_context_data(self, **kwargs):
    context = super().get_context(**kwargs)
    context['name'] = 'Sonam'
    context['roll'] = 101
    return context

# urls.py
urlpatterns = [
  path('home/', views.HomeView.as_view(), name='home'),
]
```

TemplateView With Extra Context

```python
# views.py
from django.views.generic.base import TemplateView
class HomeView(TemplateView):
  template_name = 'school/home.html'

  def get_context_data(self, **kwargs):
    context = super().get_context(**kwargs)
    context['name'] = 'Sonam'
    context['roll'] = 101
    return context

#urls.py
urlpatterns = [
  path('home/', views.HomeView.as_view(extra_context={'course':'python'}), name='home'),
]
```
