## SERIALIZER AND SERIALIZATION IN DJANGO REST FRAMEWORK

Python JSON
```text
Python has a build in package called json,
 which is used to work with json data

methods
dumps(data)  This is used to convert python object into json string.
Example
To use json package First we have to import it.
import json
python_data = {'name':'Anish','roll':101}
json_data = json.dumps(python_data)
python(json_data)
{"name":"Anish","roll":101} // json data in double quotation

loads(data)  This is used to parse json string
Example: - 
import json
json_data = {"name":"Anish","roll":101}
parsed_data = json.loads(json_data)
print(parsed_data)
{'name':'Anish','roll':101}
```

What we learned
```text
Convert python data to json , dumps() method
convert json data to python , loads() method
```

## Serializers

```text
serializers does serialization and deserialization
```
About serializers
```text
In django REST Framework, serializers are reponsible for converting complex data
such as querysets and model instances to native Python datatypes (called serialization)
that can then be easily rendered into JSON, XML or other content types which is 
understandable to Front End.
```

Deserialization done by serializers
```text
allows parsed data to be converted back into complex types 
after first validating the incoming data.
```

Ways to do Serializer Class
```text
A serializer class is very similar to a Django Form and ModelForm class, and includes
similar validation flags on the various fields, sich as required, max_length and default.

Django Rest Framework provides a Serializer class which gives you a powerful, 
generic way to control the output of your responses, as well as ModelSerializer class
which provides a useful shortcut for creating serializers that deal with model instances 
and querysets.
```


How to create serializer class
```text
- Create a seperate serializers.py file to write all serializers
```

```python
from rest_framework import serializers
class StudentSerializer(serializers.Serializer):
	name = serializers.CharField(max_length = 100)
	roll  = serializers.IntegerField()
	city  = serializers.CharField(max_length = 100)
```

models.py
```python
from django.db import models
class Student(models.Model):
	name = models.CharField(max_length = 100)
	roll = models.IntegerField()
	city = models.CharField(max_length = 100)
// then migrate the database
```

Process
``text
Convert python data to json data to client 
Convert client json data to python 
```

For example
```text
We have a table 
in this table 
one row data means one model object data
row1 is model object 1
row2 is model object 2
row3 is model object 3

model object means model instance
model instance means complex data type
```

Complex Data Type  ----convert-->Python Native DataType  ----convert--------->Json Data
		 serialization			render into json


## Serialization 
```text
The process of converting complex data such as querysets and model instances to 
native Python datatypes are called as Serialization in DRF.
```

Model data set object

Serializing model data

```text
Creating model instance stu
stu = Student.objects.get(id = 1)

Converting model instance stu to Python Dict/ Serializing Object
serializer = StudentSerializer(stu)
```

Serializing Querydata set

```text
Creating Query Set
stu  = Student.objects.all()

Creating Query Set stu to List of Python Dict/Serializing Query Set
serializer = StudentSerializer(stu, many = True)
// many before that are lots of data
```

To see data in serializer
```text
This is serialized data
serializer.data
```

JSONRenderer
```text
This is used to render Serialized data into JSON
which is understandable by Front End.

Why to do this because front only understand json
To use this you need to import JSONRenderer
from rest_framework.renderers import JSONRenderer

After this render the data into json
json_data = JSONRenderer().render(serializer.data)
``


Revision
```text
3 steps
convert the model object to python dict and convert into json data
model object
stu = Student.object.get(id=1)
serializer = StudentSerializer(stu)
json_data = JSONRenderer().render(serializer.data)
```

JSONResponse() method 
```text
syntax
JsonResponse (data,encorder = DjangoJSONEncoder, safe = True, json_dumps_params = None,**kwargs)

An HttpResponse subclass that helps to create a JSON-encoded response.
It inherits most behavior from its superclass with a couple differences:
- Its default Content-Type header is set to application/json.
 - The first paramter, data should be a dict instance.
If the safe parameter is set to False it can be any JSON-serializable to object.
- The encoder, which defaults to django.core.serializers.json.DjangoJSONEncoder, will be used 
to serializer the data.
- default value of safe is True. If safe is false any object can be passed for serialization(otherwise
only dict instances are allowed). If safe is True and a non-dict object is passed as the first argument, 
a TypeError will be raised.
- The json_dumps_params parameter is a dictonary of keyword arguments to pass to the 
json.dumps() call used to generate the response.
```



## Conclusion of the theory is to remember the below infomation
Revision
```text
3 steps
convert the model object to python dict and convert into json data
model object
stu = Student.object.get(id=1)  
serializer = StudentSerializer(stu)
json_data = JSONRenderer().render(serializer.data)
---------------------------------------------------------------------------------
| id | Name      | Roll | City             |  
| 1  | Anish       | 101 | Itahari 	      |  <-----------Model object 1
| 2  | Ronaldo  | 102 | Portugal    |   <-----------Model object 2
| 3  | Messi      |  103 | Argentina |   <-----------Model object 3

Model Object 1 converted to Python Dict  converted to Json Data
and the above are the statement to convert 
```
