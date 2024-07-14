 # Relations between serializers 

 Coding Part 

 admin.py
 ```python
from django.contrib import admin
from .models import Singer, Song

@admin.register(Singer)
class SingerAdmin(admin.ModelAdmin):
    list_display = ['id','name','gender']

@admin.register(Song)
class SongADmin(admin.ModelAdmin):
    list_display = ['id','title','singer','duration']
```

models.py
```python
from django.db import models

## many to one relation
class Singer(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Song(models.Model):
    title = models.CharField(max_length=100)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name='song')
    duration = models.IntegerField()

    def __str__(self):
        return self.title
```

serializers.py
```python
from .models import Singer, Song
from rest_framework import serializers

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id','title','singer','duration']

class SingerSerializer(serializers.ModelSerializer):
    # song = serializers.StringRelatedField(many=True, read_only=True) # this will give you the songs when you look for singer
    # song = serializers.PrimaryKeyRelatedField(many=True, read_only=True) # this will let you see the song it 
    # song = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='song-detail') # this will give you the link of the song 
    # song = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title') # you will get the model fields like song title , duration etc. of that model 
    # song = serializers.HyperlinkedIdentityField(view_name='song-detail') # gives only one link
    class Meta:
        model = Singer
        fields = ['id','name','gender','song']
```

views.py
```python
from django.shortcuts import render
from .serializers import SingerSerializer, SongSerializer
from rest_framework import viewsets
from .models import Singer, Song

class SingerViewSet(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
```

settings.py
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'api',
]
```

urls.py
```python
from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('singer', views.SingerViewSet, basename = 'singer')
router.register('song', views.SongViewSet, basename = 'song')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')), 
]
```

How it looks in browseable api
```text
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "singer": "http://127.0.0.1:8000/singer/",
    "song": "http://127.0.0.1:8000/song/"
}
```

