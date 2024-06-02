## Hotel Management System 

Model of the application
```python
from django.contrib.auth.models import User
from django.db import models
import uuid

# Create your models here.
class BaseModel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    # this model will be an abstract base class
    class Meta:
        abstract = True

# many to many field to amenities
class Amenities(BaseModel):
    amenity_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.amenity_name

class Hotel(BaseModel):
    hotel_name = models.CharField(max_length=100)
    hotel_price = models.IntegerField()
    description = models.TextField() # textfield because it can become larger
    amenities = models.ManyToManyField(Amenities) # many to many relation to Hotel
    room_count = models.IntegerField(default=10)

    def __str__(self) -> str:
        return self.hotel_name

class HotelImages(BaseModel):
    hotel = models.ForeignKey(Hotel, related_name="images", on_delete=models.CASCADE)
    images = models.ImageField(upload_to="hotels")  # corrected argument

class HotelBooking(BaseModel):
    hotel = models.ForeignKey(Hotel, related_name="hotel_bookings", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="user_bookings", on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    booking_type = models.CharField(choices=(('Pre Paid', 'Pre Paid'), ('Post Paid', 'Post Paid')), max_length=10)  # added max_length for CharField

```

Login and registration Feature

login
```html
{% extends "base.html" %}

{% block start %}

<div class="container mt-5 pt-5 col-6">
    <form method="POST">
        {% csrf_token %}
        {% include "messages.html" %}
        <div class="mb-3">
          <label for="exampleInputEmail1" class="form-label">Email address</label>
          <input type="text" name="username" required class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
          <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
        </div>
        <div class="mb-3">
          <label for="exampleInputPassword1" class="form-label">Password</label>
          <input type="password" name="password" class="form-control" id="exampleInputPassword1">
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
      </form>
</div>
{% endblock %}
```
Registration
```html
{% extends "base.html" %}

{% block start %}

<div class="container mt-5 pt-5 col-6">
    <form method="POST">
        {% csrf_token %}
        {% include "messages.html" %}
        <div class="mb-3">
          <label for="exampleInputEmail1" class="form-label">Email address</label>
          <input type="text" name="username" required class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
          <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
        </div>
        <div class="mb-3">
          <label for="exampleInputPassword1" class="form-label">Password</label>
          <input type="password" name="password" class="form-control" id="exampleInputPassword1">
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
      </form>
</div>
{% endblock %}
```

Messages
```html
{% if messages %}
{% for message in messages %}
<div class="alert alert-{{ message.tags }}" role="alert">
    {{ message }}
  </div>
  {% endfor %}
{% endif %}
```


Views 
```python
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login
# Create your views here.

def home(request):
    return render(request,'home.html')

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username = username)

        # if username does not exist
        if not user_obj.exists():
            messages.warning(request,'Account not found')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
        user_obj = authenticate(username = username, password = password)
        if not user_obj:
            messages.warning(request,'Invalid password')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
        login(request, user_obj)
        return redirect('/')
    
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    return render(request,'login.html')

def register_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username = username)

        # if username already exists
        if user_obj.exists():
            messages.warning(request,'Username already exists')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        # creating user
        user = User.objects.create(username = username)
        user.set_password(password)
        user.save()
        return redirect('/login')

    return render(request,'register.html')
```

url
```python
from django.urls import path
from .views import *

urlpatterns = [
    path('', home , name = 'home'),
    path('login/',login_page, name='login_page'),
    path('register/',register_page,name='register_page'),
]
```
