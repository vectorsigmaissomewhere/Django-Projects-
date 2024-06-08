## DeSerialization

definition
```text
Serializers are also responsible for deserialization 
which means it allows parsed data to be converted 
back into complex types, after validating the incoming data
```

process
```text
jsondata ----->Python Native Datatype---------->ComplexDataType

first parse data then do de-serialization
```
Things to learn before doing de-serialization

1)  BytesIO()
```text
A stream implementation using an in-memory bytes buffer.
It inherits BufferedIOBase. The buffer is discarded when the 
close() method is called.

How to implement
import io
stream = io.BytesIO(json_data)
```

2) JSONParser()
```text
This is used to parse json data to python native data type

How to implement
from rest_framework.parsers import JSONParser
parsed_data = JSONParser().parse(stream)
```

3) De-serialization
```text
De-serialization allows parsed data to be converted back
into complex types, after first validating the incoming data.

How to implement
Creating Serializer Object
serializer = StudentSerializer(data  = parsed_data)

Validated Data
serializer.is_valid()

serializer.validated_data
serializer.errors
```

4) serializer.validated_data
```text
This is the Valid data
serializer.validated_data
```

That's the end


## Create Data/Insert Data
```python
from rest_framework import serializers
class StudentSerializer(serializers.Serializer):
	name  = serializers.CharField(max_length = 100)
	roll = serializers.IntegerField()
	city  = serializers.CharField(max_length = 100)

	def create(self, validate_data):
		return Student.objects.create(**validate_data)
```

## Coding part 

## main objective : other company application sending data into our application
sending data from frontend
```text
myapp.py is sending post request to views.py
and the data is coming to views.py
```
