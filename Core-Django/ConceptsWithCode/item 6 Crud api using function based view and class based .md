## CRUD API USING FUNCTION BASED VIEW AND CLASS BASED VIEW IN DJANGO REST FRAMEWORK

1 ) update data

can be done in two ways
partial update: updating only one column field
complete update: updating all column field

how to do
```python 
from rest_framework import serializers
class StudentSerializer(serialzers.Serializer):
    name  = serializers.CharField(max_length = 100)
    roll = serializers.IntegerFIeld()
    city  = serializers.CharField(max_length = 100)
    """instance: Here instance means old data stored in database
         validated_data: New data from user for updation, what you need to update
     """
    def update(self, instance, validated_data):
       # if name is new it will go to instance.name
        instance.name = validated_data.get('name',instance.name)
        instance.roll = validated_data.get('roll',instance.roll)
        instance.city = validated_data.get('city',instance.city)
        instance.save()
        return instance
```

How to do complete update data
```text
By default, serializers must be passed values for all required fields or they 
will raise validation errors. means you can't do partial update
```
```python 
#Required all data from front end/client
serializer = StudentSerializer(stu,data = pythondata)
if serializer.is_valid():
    serializer.save()
```

to partial update data
means all data not required
```python 
serializer = StudentSerializer(stu,data = pythondata, partial=True)
if serializer.is_valid():
    serializer.save()
```


## First Program get all the data into third party application
admin.py
```python
from django.contrib import admin
from .models import Student

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll','city']
```

models.py
```python
from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)
```

serializers.py
```python
from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'roll', 'city']
```

views.py
```python
from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def student_api(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id', None)
        if id is not None:
            try:
                stu = Student.objects.get(id=id)
                serializer = StudentSerializer(stu)
                return JsonResponse(serializer.data)
            except Student.DoesNotExist:
                return JsonResponse({'error': 'Student not found'}, status=404)
        
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return JsonResponse(serializer.data, safe=False)
```

urls.py
```python
from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/',views.student_api),
]
```

myapp.py
```python
import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"

def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}

    r = requests.get(url=URL, json=data)
    try:
        r.raise_for_status() 
        data = r.json()
        print(data)
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")
    except ValueError:
        print("Response content is not valid JSON")

get_data(1)
```


output
```text
{'id': 1, 'name': 'Ronaldo', 'roll': 7, 'city': 'Lisbon'}
```
