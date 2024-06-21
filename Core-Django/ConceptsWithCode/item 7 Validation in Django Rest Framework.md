## Validation

Three types of writing validation
```text
Field Level Validation
Object Level Validation
Validators
```
1 Field Level Validation
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
