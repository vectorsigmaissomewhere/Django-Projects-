
## Many to One Relationship in Django
```text
When one or more row of table B can be linked to one row of table A.

Many to One Relationship - To define a many-to-one relationship, use ForeignKey. You use it just
like any other Field type: by including it as a class attribute of your model.

A many-to-one relatioship requires two positional arguments: the class to which the model is 
related and the on_delete option. 

Syntax:- ForeignKey(to, on_delete, **options)

to - The class to which the model is related.
on_delete - When an object referenced by a ForeignKey is deleted, Django will emulate
the behavior of the SQL constraint specified by the on_delete argument. on_de;ete doesn't create an
SQL constraint in the database.

limit_choices_to - Sets a limit to the available choices for this field when thsi field is 
rendered using a ModelForm or the admin (by default, all objects in the queryset are available
to choose). Either a dictionary, a Q object, or a callable returning a dictionary or Q object can 
be used.

related_name - The name to use for the relation from the related back to this one. It's also the 
default value for related_query_name(the name to use for the reverse filter name from the target model.)
If you'd prefer Django not to create a backwards relation, set related_name to '+' or end it with
'+'.

related_query_name - The name to use for the reverse filter name from the target model. If defaults
to value of related_name or default_related_name if set, otherwise it defaults to the name of the
model.

to_fiel - The field on the related object that the relation is to. By default, Django uses the primary
key of the related object. If you reference a difference field, that field must have unique=True.

swappable - Controls the migration framework's reaction if the ForeignKey is pointing at a 
swappable model. If it is True - the default - then if the ForeignKey is pointing at a model which
matches the current value of settings.AUTH_USER_MODEL(or another swappable model setting)
the relationship will be stored in the migration using a reference to the setting, not to the model
directly.

db_constraint - Controls whether or not a constraint should be created in the database for this 
foreign key. The default is True, and that's almost certainly what you want; setting this to False
can be very bad for data integrity. That said, here are some scenarios where you might want to do 
this:
You have legacy data that is not valid.
You're sharding your database.
If this is set to False, accessing a related object that doesn't exist will raise its DoesNotExist
exception.

on_delete - When an object referenced by a ForeignKey is deleted, Django will emulated the 
behavior of the SQL constraint specified by the on_delete argument, on_delete doesn't create 
an SQL constraint in the database.
The possible values for on_delete are found in django.db.models"
- CASCADE - Cascade deletes. Django emulates the behavior of the SQL constraint ON DELETE CONSTRAINT
also deletes the object containing the ForeignKey.
- PROTECT - Prevent deletion of the referenced object by raising ProtectedError, a subclass of 
django.db.IntegrityError.
- SET_NULL - Set the ForeignKey null; this is only possible if null is True.
- SET_DEFAULT - Set the ForeignKey to its default value; a default for the ForeignKey must be set.
- SET() - Set the ForeignKey to the value passed to SET(), or if a callable is passed in, the result 
of calling it.
- DO_NOTHING - Take no action. If you database backend enforces referential integrity, this will cause
an IntegrityError unless you manually add an SQL ON DELETE constraint to the database field.
```

Example
```python
class User(models.Model):
    user_name = models.CharField(max_length=70)
    password = models.CharField(max_length=70)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=70)
    post_cat = models.CharField(max_length=70)
    post_publish_data = models.DateField()
```

## Coing Part
```python
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.PROTECT) # doing this user cannot be deleted
    # user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) # doing this if user is deleted post cannot be deleted6  
    post_title = models.CharField(max_length=70)
    post_cat = models.CharField(max_length=70)
    post_publish_date = models.DateField()
```

Where to find the full code
```text
check onetomanyrelationship
```
