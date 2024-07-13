## OrderingFilter

about
```text
The OrderingFilter class supports simple parameter controlled ordering of 
results.

http://127.0.0.1:8000/studentapi/?ordering=name

The client may also specify reverse orderings by prefixing the field name
with '-', like so:
http://127.0.0.1:8000/studentapi/?ordering=-name

Multiple orderings may also be specified:
http://example.com/api/users?ordering=account, username
```

How to implement OrderingFilter
```text
It's recommended that you explicitlu specity which fields the API should allowing in the ordering filter. You can do this by setting an ordering_fields
attribute on the view, like so:

class StudentListView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [OrderingFilter] 
    ordering_fields = ['name']
    ordering_fields =['name','city']
    ordering_fields = '__all__'
```


## Coding For Ordering Filter in Django REST Framework

views.py
```
from .serializers import StudentSerializer
from .models import Student
from rest_framework.generics import ListAPIView
from rest_framework.filters import OrderingFilter

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [OrderingFilter]
```
Text
```
Now you can get bunch of options for filtering
```

If you want to do filtering to specific field

views.py
```python
from .serializers import StudentSerializer
from .models import Student
from rest_framework.generics import ListAPIView
from rest_framework.filters import OrderingFilter

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [OrderingFilter]
    OrderingFilter = ['name']
```

If you want to do filtering to multiple fileds

views.py
```python
from .serializers import StudentSerializer
from .models import Student
from rest_framework.generics import ListAPIView
from rest_framework.filters import OrderingFilter

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [OrderingFilter]
    OrderingFilter = ['name','city']
```

How the link look like
```text
http://127.0.0.1:8000/studentapi/?ordering=city
````

Conclusion
```text
From here we learned to filter data from ascending to descending and vice-versa
```
