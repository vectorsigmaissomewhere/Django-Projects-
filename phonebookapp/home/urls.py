from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('login/',login_page,name='login_page'),
    path('register/',register_page,name='register_page'),
    path('addContact/',addContact,name='addContact'),
    path('viewContact/',viewContact,name='viewContact'),
    path('logout/', logout_view, name='logout_view'),
]
