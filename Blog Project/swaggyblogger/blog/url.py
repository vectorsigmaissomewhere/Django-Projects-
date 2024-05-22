from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('home',views.home,name='home'),
    path('',views.login,name='login'),
    path('register/',views.register,name='register'),
]
