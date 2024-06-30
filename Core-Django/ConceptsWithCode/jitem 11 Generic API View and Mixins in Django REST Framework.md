# Generic API View and Mixins in Django REST Framework 

about
```text
we will use whatever that is made in rest_framework

This class extends REST framework's APIView class, adding commonly
required behavior for standard list and detail views.

Attributes:
queryset - The queryset that should be used for returning objects from this view.
 Typically, you must either set this attribute, or override the get_queryset() method.
If you are overriding a view method, It is important that you can get_queryset() instead of
accessing this property directly, as queryset will get evaluated once, those results will be
cached for all subsequent requests.
means use this attribute and set objects or use the methods to set the object

serializer_class - The serializer class that should be used for validating and
deserializing input, and for serializing output. Typically, you must either set this attribute,
or override the get_serializer_class() method.

lookup_field - The model field that should be used to for performing object lookup of
individual model instances. Defaults to 'pk'.

lookup_url_kwarg - The URL keyword argument that should be used for object lookup.
 The URL conf should include a keyword argument corresponding to this value.
If unset this defaults to using the same value as lookup_field.

pagination_class  - The pagination class that should be used when paginating list results.
Defaults to the same value as the DEFAULT_PAGINATION_CLASS setting, which is 'rest_framework.pagination.
PageNumberPagination'.Setting pagination_class = None will disable pagination on this view.

filter backends  - A list of filter backend classes that should be used for filtering the queryset.
Defaults to the same value as the DEFAULT FILTER BACKENDS setting.
```

Methods
```text
get_queryset(self) - It returns the queryset that should be used for list views,
and that should be used as the base for lookups in detail views. Defaults to returning the queryset
specified by the queryset attribute.

This method should always be used rather than accessing self.queryset directly,
as self.queryset gets evaluated only once, and those results are cached for all subsequent requests.

get_objects(self) - It returns an object instance that should be used for detail views.
 Defaults to using the lookup_field parameter to filter the base queryset. 

get_serializer_class(self) - It returns the class that should be used for the serializer.
 Defaults to returning the serializer_class attribute.

get_serializer_context(self) - It returns a dictionary containing any extra context
 that should be supplied to the serializer. Defaults to including 'request'.'view' and 'format' keys.

get_serializer(self, instance = None, data = None, many = False, partial = False) -
It returns a serializer instance.

get_paginated_response(self, data) - It returns a paginated style Response object.

paginated_queryset(self, queryset) - Paginate a queryset if required, either returning a page object,
 or None if pagination is not configured for this view.

filter_queryset(self, queryset) - Given a queryset, filter it with whichever filter backends are in use,
returning a new queryset.
```

about method
```text
most of the methods are automatically generated and implemented
but if you need some modification you make chnage in get_queryset().
```

what is queryset()
```text
returing all data of a table at a time
```

Mixins
```text
using class-based views allows us to easily compose reusable bits of behaviour.
The create/retrieve/update/delete operations that we've been using so far are 
going to be pretty similar for any model-backed API views we create.

Those bits of common behaviour are implemented in REST framework's mixin classes.
 The mixin classes provide the action methods rather than defining the handler
methods, such as get() and post(), directly. This allows for more flexible 
composition of behavior.

The mixin classes can be imported from rest_framework.mixins

List of mixin classes:
1 - ListModelMixin
2 - CreateModelMixin
3 - RetrieveModelMixin
4 - UpdateModelMixin
5 - DestroyModelMixin
```

1 ListModelMixin
```text
It provides a list(request, *args, **kwargs) method, the implements listing a queryset.

If the queryset is populated, this return a 200 OK response, with a serialized 
representation of the queryset as the body of the response. The response data may 
optionally be paginated.

from rest_framework.mixins import ListModelMixin
from rest_framework.generics import GenericAPIView
```

Example of ListModelMixin
about
```text
write 4 lines and get all the data
```
```python
from rest_framework.mixins import ListModelMixin
from rest_framework.generics import GenericAPIView
class StudentList(ListModelMixin, GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)	
```

2 CreateModelMixin
```text
It provides a create(request, *args, **kwargs) method, that implements creating and 
saving a new model instance.

If an object is created this returns a 201 Created response, with a serialized
representation of the object as the body of the response. If the representation
contains a key named url, then the Location header of the response will be
 populated with the value. 

If the request data provided for creating the objects was invalid, a 400 Bad Request
response will be returned, with the error details as the body of the response.
```

Example of CreateModelMixin
```python
from rest_framework.mixins import CreateModelMixin
from rest_framework.mixins import GenericAPIView
class StudentCreate(CreateModelMixin, GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
```

3 RetrieveModelMixin
about
```text
It provides a retrieve(request, *args, **kwargs) method, the implements returning 
and existing model instance in a response.

If an object can be retrieved this returns a 200 OK response, with a serialized
representation of the object as the body of the response. Otherwise it will return a 
404 Not found.
```

Example of RetrieveModelMixin
```python
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.generics import GenericAPIView
class StudentRetrieve(RetrieveModelMixin, GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerialier
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
```

4 UpdateModelMixin

about
```text
It provides a update(request, *args, **kwargs) method, that implements updating
and saving an existing model instance.

It also provides a partial_update(request, *args, **kwargs) method, which is similar
to the update method, except that all fields for the update will be optional. This 
allows support for HTTP PATCH requests.

If an object is updated this returns a 200 OK response, with a serialized
representation of the object as the body of the respone.

If the request data provided for updating the object was invalid, a 400 Bad Request
response will be returned, with the error details as the body of the reponse.
```

Example of UpdateModelMixin
```python
from rest_framework.mixins import UpdateModelMixin
from rest_framework.generics import GenericAPIView

class StudentUpdate(UpdateModelMixin, GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
```

5 DestoryModelMixin
about
```text
It provides a destroy(request, *args, **kwargs) method, that is implemented deletion of 
an existing model instance.

If an object is deleted this returns a 204 No Content response, otherwise it will
return a 404 Not Found.
```

Example of DestroyModelMixin
```python
from rest_framework.mixins import DestroyModelMixin
from rest_framework.generics import GenericAPIView
class StudentDestory(DestroryModelMixin, GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def delete(self, request, *args, **kwargs):
        return self.destrory(request, *args, **kwargs)
```

# 1 Coding Part using Generic API View And Model Mixin

things to remember before looking to code
```text
Mixin is same as other way of creating and api which is present in jitem 10
Generic API View and Model Mixin makes your code shorter in comparison to
Class Based api view and function based api view

also mixin provides a form to create data, update data etc.
```

which part of jitem10 you should work on to 
```text
work in views.py and urls.py only 
```

views.py
```python
# GenericAPIView and Model Mixin
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin # list all the data
from rest_framework.mixins import CreateModelMixin # used to making data
from rest_framework.mixins import RetrieveModelMixin # used to retrived data accoding to id passed in url
from rest_framework.mixins import UpdateModelMixin # updates the data
from rest_framework.mixins import DestroyModelMixin # used to delete the data

# used to get all the data
class StudentList(GenericAPIView, ListModelMixin):
    queryset = Student.objects.all() # getting all queryset
    serializer_class = StudentSerializer
    
    # method that lists all the data from Student Model
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs) 

# used in creating data
class StudentCreate(GenericAPIView, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # method that helps in creating data 
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

# retrieve data according to the url passed
class StudentRetrive(GenericAPIView, RetrieveModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, * args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

# use to update the data  
class StudentUpdate(GenericAPIView, UpdateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # this works for both put and patch 
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


# use to delete the data
class StudentDestroy(GenericAPIView, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
```

urls.py
```python
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/',views.StudentList.as_view()), # as it is class based api views # url for listing data
    # path('studentapi/',views.StudentCreate.as_view()), # used for creating data
    # path('studentapi/<int:pk>/',views.StudentRetrive.as_view()), # retrieving data
    # path('studentapi/<int:pk>/',views.StudentUpdate.as_view())#use to update the data
    path('studentapi/<int:pk>/', views.StudentDestroy.as_view())# use to delete the data
    # path('studentapi/<int:pk>',views.StudentAPI.as_view()),
]
```

keypoints
```text
you have to create a seperate url for each crud operation in this which is a problem
this problem is solved in below program 
```
