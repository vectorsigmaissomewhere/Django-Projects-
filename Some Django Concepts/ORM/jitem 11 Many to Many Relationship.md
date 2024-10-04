## Many to Many Relationship
```text
When one row of table A can be linked to one or more rows if table B, and vice-versa.

Many to Many Relationships - To define a many-to-many relationship, use ManyToManyField. You 
use it just like any other Field type: by including it as a class attribute of your model.

ManyToManyField requirs a positional argument: the class to which the model is related.
Syntax:- ManyToManyField(to, **options)

Rest is similar to any other relationship
```

Example
```python
class User(models.Model):
    user_name = models.CharField(max_length=70)
    password = models.CharField(max_length=70)

class Song(models.Model):
    user = models.ManyToManyField(User)
    song_name = models.CharField(max_length=70)
    song_duration = models.IntegerField()
```

models.py
```python
from django.db import models
from django.contrib.auth.models import User

class Song(models.Model):
    user = models.ManyToManyField(User)
    song_name = models.CharField(max_length=70)
    song_duration = models.IntegerField()

    def written_by(self):
        return ",".join([str(p) for p in self.user.all()]) 
```

admin.py
```python
from django.contrib import admin
from .models import Song

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['song_name', 'song_duration', 'written_by']
```

Where to find the full code for this
```text
no project folder made for this
```
