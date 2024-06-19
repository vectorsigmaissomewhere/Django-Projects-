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


## 2 FUNCTION BASED CRUD OPERATION IN DJANGO 
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
    # create data 
    def create(self,validated_data):
        return Student.objects.create(**validated_data)
    
    # implementing update method
    def update(self, instance,validated_data):
        # means if user provides data put it in here 
        print(instance.name)
        instance.name = validated_data.get('name',instance.name)
        print(instance.name)
        instance.roll = validated_data.get('roll',instance.roll)
        instance.city = validated_data.get('city',instance.city)
        instance.save()
        return instance
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

@csrf_exempt
def student_api(request):
    # geting the data according to the user id 
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
    
    # saving the data 
    if request.method == 'POST':
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
    
    # updating the data
    if request.method == 'PUT':
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
    
    # deleting the data, no work of serializer in this place
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id = id)
        stu.delete()
        # sending response of the data is deleted
        res = {'msg': 'Data Deleted!!'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data,content_type = 'application/json')
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

# get_data(1)

# this function will send data to the server and save it into table 
# this is in dictionary form 
def post_data():
    data = {
        'name':'Ravi',
        'roll':104,
        'city':'Dhanbad'
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
        'id': 7,
        'name': 'Rohit',
        'city': 'Ranchi'
    }

    json_data = json.dumps(data)
    r = requests.put(url = URL, data = json_data)
    data = r.json()
    print(data)

# update_date()

# this function will delete the data based on id 
def delete_data():
    data = {'id':3}

    json_data = json.dumps(data)
    r = requests.delete(url = URL, data = json_data)
    data = r.json()
    print(data)
delete_data()
```


output
```text
the third party application user will get message like data deleted
```


## 4 CLASS BASED CRUD OPERATION IN DJANGO 

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

# get_data(1)

# this function will send data to the server and save it into table 
# this is in dictionary form 
def post_data():
    data = {
        'name':'Bhabi',
        'roll':104,
        'city':'Dhanbad'
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
        'id': 6,
        'name': 'Kavi',
        'city': 'Ranchi'
    }

    json_data = json.dumps(data)
    r = requests.put(url = URL, data = json_data)
    data = r.json()
    print(data)

update_date()

# this function will delete the data based on id 
def delete_data():
    data = {'id':7}

    json_data = json.dumps(data)
    r = requests.delete(url = URL, data = json_data)
    data = r.json()
    print(data)
delete_data()
```

serializers.py
```python
from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'roll', 'city']
    # create data 
    def create(self,validated_data):
        return Student.objects.create(**validated_data)
    
    # implementing update method
    def update(self, instance,validated_data):
        # means if user provides data put it in here 
        print(instance.name) # what data was earlier
        instance.name = validated_data.get('name',instance.name)
        print(instance.name) # what data is now 
        instance.roll = validated_data.get('roll',instance.roll)
        instance.city = validated_data.get('city',instance.city)
        instance.save()
        return instance
```
