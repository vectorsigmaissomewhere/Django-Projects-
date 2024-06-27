ModelSerializer Class

about
```text
The ModelSerializer class provides a shortcut that lets you automatically create a
Serializer class with fields that correspond to the Model fields.

The ModelSerializer class is the same as a regular Serializer class, except that:
- It will automatically generate a set of field for you, based on the model.
- It will automatically generate validators for the serializer, such as unique_together 
validators.
- It includes simple default implementations of create() and update().
```
Example to create ModelSerializer Class

Create a seperate serializers.py file to write all serializers
```python 
from rest_framework import serializers
class StudentSerializer(serializer.ModelSerializer):
    class Meta:
        model  = Student
        fields = ['id','name','roll','city']
# to include all user
# fields = '__all__'
# exclude = ['roll']
```

Important point to learn in this topic
```text
We will make other files same and will work only in serializers.py
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

admin.py
```python
from django.contrib import admin
from .models import Student

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll','city']
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
# we have to send csrf token whenever you make post request 
# but we cannot do this from here so , we will use csrf_exempt
from django.views.decorators.csrf import csrf_exempt 
# when making class based use method_decorator
from django.utils.decorators import method_decorator
from django.views import View

@method_decorator(csrf_exempt,name='dispatch')
class StudentAPI(View):
    def get(self, request, *args, **kwargs):
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
    
    def post(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data) 
        pythondata = JSONParser().parse(stream) # getting python data
        serializer = StudentSerializer(data = pythondata) # converting into complex object
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type = 'application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type = 'application/json')
    
    def put(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream) # convert stream data into parsed data
        id = pythondata.get('id') # get the id
        stu = Student.objects.get(id = id)
        serializer = StudentSerializer(stu, data = pythondata, partial = True) # update partial data , if False need to update all data
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data updated !!'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type = 'application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type = 'application/json')
    
    def delete(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id = id)
        stu.delete()
        # sending response of the data is deleted
        res = {'msg': 'Data Deleted!!'}
        # json_data = JSONRenderer().render(res)
        # return HttpResponse(json_data,content_type = 'application/json')
        # making code smaller
        return JsonResponse(res,safe=False)
```

myapp.py
```python
import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"

# this function will give you the data according to the id 
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

#get_data()

# this function will send data to the server and save it into table 
# this is in dictionary form 
def post_data():
    data = {
        'name':'Shownum',
        'roll':109,
        'city':'Dhanchad'
    }
    # converting this into json form 
    json_data = json.dumps(data)
    r = requests.post(url = URL, data = json_data)
    data = r.json()
    print(data)

# post_data()


# this function will update the data with id
# this is a partial updates as only required data is updated 
def update_date():
    data = {
        'id': 9,
        'name': 'Thavi',
        'roll': 111,
        'city': 'banchi'
    }

    json_data = json.dumps(data)
    r = requests.put(url = URL, data = json_data)
    data = r.json()
    print(data)

update_date()

# this function will delete the data based on id 
def delete_data():
    data = {'id':6}

    json_data = json.dumps(data)
    r = requests.delete(url = URL, data = json_data)
    data = r.json()
    print(data)
#delete_data()
```

urls.py
```python
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/',views.StudentAPI.as_view()),
]
```


## 1 ModelSerializer Class use
```text
Create method and update method is automatically available
when using model serializer you don't need to
create the method
```
Showing with Example
```python
from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name','roll','city']
    # create method and update method can be done by itself
```

## 2 read-only use in ModelSerializer
```text
read-only means you can't update it
you can only read it
```
this example shows how you can use read-only in multiple ways
```python
from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(read_only=True) # name will not change because we have made it read-only
    class Meta:
        model = Student
        fields = ['name','roll','city']
    # create method and update method can be done by itself
    # read_only_fields = ['name','roll'] # making multiple fields read-only
    # using kwargs to make ready-only 
    extra_kwargs = {'name':{'read-only':True}}
```


## 2 ModelSerializer Validation
this example shows how you can use validation in Model Serializer
```text
In this example you name must start your name with r
and your roll number must be less than 200
```
serializer.py
```python
from rest_framework import serializers
class StudentSerializer(serializers.ModelSerializer):
    def start_with_r(value):
        if value[0].lower() != 'r':
            raise serializers.ValidationError('Name should be start with R')
    name = serializers.CharField(validators=[start_with_r])
    class Meta:
        model = Student
        fields = ['id','name','roll','city']

    # field level validation
    def validate_roll(self,value):
        if value >= 200:
            raise serializers.ValidationError('Seat Full')
       return value
```
