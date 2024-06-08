## Serializer fields
```python 
from rest_framework import serializers
class StudentSerializers(serializers.Serializers):
	name = serializers.CharField(max_length = 100)
	roll = serializers.IntegerField()
	city = serializers.CharField(max_length = 100)
```
here,  CharField , IntegerFIeld are serializers fields

Definition

```text
Serializer fields handle converting between primitive values
and internal datatypes.
They also deal with validating input values, as well
as retrieving and setting the values from their parent objects.

Syntax is given above

all serializers field
CharField
IntegerField
FloatField
DecimalField
SlugField
EmailField
BooleanField
NullBooleanField
URLField
FileField
DateField
DateTimeField
DurationField
RegexField
UUIDField
FilePathField
IPAddressField
ChoiceField
MultipleChoiceField
ListField
DictField
HStoreField
JSONField
ReadOnlyField
HiddenField
ModelField
SerializerMethodField
```

## Core Arguments

list of core arguments
```text
label, validators,error_messages,help_text,required,default,
initial,style

style example 
password = serializers.CharField(max_length = 100, style={'input_type':'password','placeholder':'Password'}
)
other corearguments
read_only, write_only,allow_null,source
```
