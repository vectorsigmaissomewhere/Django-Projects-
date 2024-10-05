
Type of Views
```text
- Function Based View
- Class Based View
```

Class Based View
```text
Class-based views provide an alternative way to implement views as Python objects instead of 
functions.
They do not replace function-based views.

Two types of class based view
- Base Class-Based Views/ Base View
- Generic Class-Based Views/ Generic View

Advantages:- 
- Organization of code related to specific HTTP methods(GET, POST, etc, ) can be addressed by
  seperate methods instead of conditional branching
- Object oriented techniques such as mixins (multiple inheritance) can be used to factor code 
  into resuable components. 
```

Base Class-Based View
```text
Base class-based views can be thought of as parent views, which can be used by themselves or 
inherited from. They may not provide all the capabilities required for projects, in which case 
there are Mixins which extend what base views can do.
- View
- Template View
- RedirectView
```

View
```text
django.views.generic.base.View
The master class-based base view. All other class-based views inherit from this base. It isn't 
strictly a generic view and thus can also be imported from django.views.

generic is in 
Lib\site-packages\django\views\generic in Python

Attribute:- 
http_method_names = ['get', 'post', 'put, 'patch', 'delete', 'head', 'options', 'trace']
The list of HTTP method names that this view will accept.

Methods:- 
setup(self, request, *args, **kwargs) - It initializes view instance attribute: self.request, 
self.args, and self.kwargs prior to dispatch()

dispatch(self, request, *args, **kwargs) - The view part of the view - the method that accepts
a request argument plus arguments, and returns a HTTP response

The default implementation will inspect the HTTP method and attempt to delegate to a method that
matches the HTTP method; a GET will be delegated to get(), a POST to post(), and so on.

Be default, a HEAD request will be delegated to get(). If you need to handle HEAD requests in a 
different way than GET, you can override the head() method.

http_method_not_allowed(self, request, *args, **kwargs) - If the view was called with a HTTP 
method it doesn't support, this method is called instead.
The default implementation returns HttpResponseNotAllowed with a list of allowed methods in   
plain text. 

options(self, request, *args, **kwargs) - If handles responding to requests for the OPTIONS 
HTTP verb. Returns a response with the Allow header containing a list of the view's allowed 
HTTP method names.

as_view(cls, **initkwargs) - It returns a callable view that takes a request and returns a 
response.

_allowed_methods(self)
```

## Difference between function based view and class based view 

```text
in function based view you don't have to define get method
but in class based view you have to define get method
```
function based view

views.py
```python
from django.html import HttpResponse
def myview(request):
  return HttpResponse('<h1>Function Based View</h1>')
```
urls.py
```python
from django.urls import path 
from school import views 
urlpatterns = [path('func/', views.myview, name='func')]
```

class based view

views.py
```python  
from django.views import View 
class MyView(View):
  def get(self, request):
    return HttpResponse('<h1>Class Based View</h1>')
```
urls.py
```python 
from django.urls import path 
from school import views 
urlpatterns = [
  path('cl/', views.MyView.as_view(), name='cl'),
]
```

how urls.py in class based view works
```text
MyView.as_view() is called when request is called 
and this function creates an instance and calls 
setup function to initialize attribute
and then dispatch method is called
this checks which method is this 
if the requested http method is present in the views 
it returns http response if not it returns http response 
not allowed 
```
