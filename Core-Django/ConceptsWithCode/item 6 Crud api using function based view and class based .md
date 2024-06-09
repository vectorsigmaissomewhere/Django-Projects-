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
