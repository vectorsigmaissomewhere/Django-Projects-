## Validation

Three types of writing validation
```text
Field Level Validation
Object Level Validation
Validators
```
## 1 Field Level Validation
```text
We can specify custom field-lebel validation by adding 
validate_fieldName methods to your Seerializer subclass
There are similar to django forms ,clean_fieldName methods

validate_fieldName methods should return the validated value
or raise a serializers.ValidationError

Syntax:- def validate_roll(self,value)
Example:- def validate_roll(self,value)
Where, value is the field value that requires validation
```

Example of Field Level Validation
```python 
from rest_framework import serializers
class StudentSerializer(serializers.Serializers):
    name = serializers.CharField(max_length = 100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length = 100)

    # if user enters more than 200 value then  , it will give the below validation error, making post requestc 
    def validate_roll(self,value): # if the value has more than 200 value
        if value >= 200:
            raise serializers.ValidationError('Seat Full')
            return value
```
About the above example
```text
the validate_roll method is called automatically when is_valid() method is called
```
Conclusion on the example
```text
If you want to validate one field
use field level validation
```

## FIELD LEVEL VALIDATION WITH CODE EXAMPLE
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

# creating a validation for roll
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
    
    # Field Level Validation
    # implenting field level valiation for roll
    def validate_roll(self,value):
        if value >= 200:
            raise serializers.ValidationError('Seat Full')
        return value
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
        'name':'Dhoni',
        'roll':201,
        'city':'Dhanbad'
    }
    # converting this into json form 
    json_data = json.dumps(data)
    r = requests.post(url = URL, data = json_data)
    data = r.json()
    print(data)

post_data()


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

#update_date()

# this function will delete the data based on id 
def delete_data():
    data = {'id':7}

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

Console output
```text
{'roll': ['Seat Full']}
```

Conclusion of Field Level Validation
```text
- Checks the field to be validated
- in our case it is roll
- check the serializers.py for more detail
- In views.py there is a function serializer.is_valid() which is called and checks if it is validated or not

Important files to check to learn
- serializers.py
- myapp.py
- views.py
```


## 2 Object Level validation
about
```text
When we need to do validation that requires access to multiple files we
do object level validation by adding a method called validate() to 
Serializer subclass.

It raises a serializers. ValidationError if necessary, or just return the 
vaildated values.

Syntax:- def validate(self, data)
Example:- def validate(self, data)
Where, data is dictionary of field values,
```
Example
```python 
from rest_framework import serializers
class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 100)
    roll = serializers.IntegerField()
    city  = serializers.CharField(max_length  = 100)
    # data is in dictionary form 
    def validate(self,data): #method that does object validation 
        nm = data.get('name') # get the data using get method because it is in dictionary form 
        ct = data.get('city')
        if nm.lower() == 'rohit' and ct.lower() != 'ranchi': 
            raise seralizers.ValidationError('City must be Ranchi')
        return data
```
about the example program 
```text
A person named rohit must be of city ranchi
```

Example with code with FIELD LEVEL VALIDATION AND OBJECT LEVEL VALIDATION

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

# creating a validation for roll
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
    
    # Field Level Validation
    # implenting field level valiation for roll
    def validate_roll(self,value):
        if value >= 200:
            raise serializers.ValidationError('Seat Full')
        return value
     
    # Object Level Validation
    def validate(self,data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'rohit' and ct.lower() != 'ranchi':
            raise serializers.ValidationError('City must be Ranchi')
        return data
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
        'name':'rohit',
        'roll':120,
        'city':'ranchi'
    }
    # converting this into json form 
    json_data = json.dumps(data)
    r = requests.post(url = URL, data = json_data)
    data = r.json()
    print(data)

post_data()


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

#update_date()

# this function will delete the data based on id 
def delete_data():
    data = {'id':7}

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
