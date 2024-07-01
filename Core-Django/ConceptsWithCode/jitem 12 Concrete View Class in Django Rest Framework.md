## Concrete View Class
about
```text
Every kind of implementation has been made
we just have to use it 
```

Objective
```text
How to do CRUD using Concrete View Class
```

The following classes are the concrete generic views
```text
If you're using generic views this is normally the level you'll
be working at unless you need heavily customized behavior.

The view classes can be imported from rest_framework.generics.
- ListAPIView         	           
- CreateAPIView		Combination of ListAPIView and CreateAPIView is ListCreateAPIView
- RetrieveAPIView		Combination of RetrieveAPIView and UpdateAPIView is RetrieveUpdateAPIView	
- UpdateAPIView		Combination of RetrieveAPIView and DestoryAPIView is RetrieveDestroyAPIView
- DestroyAPIView		Combination of RetrieveAPIView, UpdateAPIView and DestroyAPIView is RetrieveUpdateDestroyAPIView
```

ListAPIView
```text
It is used for read-only endpoints to represent a collection of model instances. It
provides a get method handler.
Extends: GenericAPIView, ListModelMixin
Get all the objects in the form of list
```
Example
```python
from rest_framework.genrics import ListAPIView
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class  = StudentSerializer
```

CreateAPIView
```text
It is used for create-only endpoints. It provides a post method handler.
Extends: GenericAPIView, CreateModelMixin
```
Example
```python
from rest_framework.genrics import CreateAPIView
class StudentCreate(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
```

RetrieveAPIView
```text
It is used for read-only endpoints to represent a single model instance. It provides a 
get method handler.
Extends: GenericAPIView, RetrieveModelMixin
```
Example
```python
from rest_framework.genrics import RetrieveAPIView
class StudentRetrieve(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
```

UpdateAPIView
```text
It is used for update-only endpoints for a single model instance. It provide put and
patch method handlers.
Extends: GenericAPIView, UpdateModelMixin
```
Example
```python
from rest_framework.genrics import UpdateAPIView
class StudentUpdate(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
```

DestroyAPIView
```text
It is used for delete-only endpoints for a single model instance. It provides a delete
method handler.
Extends:  GenericAPIView, DestroyModelMixin
```

Example
```python
from rest_framework.generics import DestroyAPIView
class StudentDestroy(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
```

ListCreateAPIView
```text
It is used for read-write endpoints to represent a collection of model instances. It
provides get and post method handlers.
Extends: GenericAPIView, ListModelMixin, CreateModelMixin
```

Example 
```python
from rest_framework.generics import ListCreateAPIView
class StudentListCreate(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
```

RetrieveUpdateAPIView
```text
It is used for read or update endpoints to represent a single model instance. It 
provides get, put and patch method handlers.
Extends: GenericAPIView, RetrieveModelMixin, UpdateModelMixin
```

Example
```python
from rest_framework.generics import ListCreateAPIView
class StudentRetrieveUpdate(RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
```

RetrieveDestroyAPIView
```text
It is used for read or delete endpoints to represent a single model instance. It
provides get and delete method handlers.
Extends: GenericAPIView, RetrieveModelMixin, DestroyModelMixin
```

Example
```python
from rest_framework.generics import RetrieveDestroyAPIView
class StudentRetrieveDestroy(RetrieveDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
```

RetrieveUpdateDestroyAPIView
```text
It is used for read-write-delete endpoints to represent a single model instance. It
provides get, put, patch and delete method handlers.
Extends: GenericAPIView, RetrieveModelMixin, UpdateModelMixin,
DestroyModelMixin
```

Example
```python
from rest_framework.generics import RetrieveUpdateDestoryAPIView
class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
```
