from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate , login,logout
from .models import (Contact,BaseModel)
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request,'home.html')

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username = username)

        if not user_obj.exists():
            messages.warning(request, 'Account not found ')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        user_obj = authenticate(username = username , password = password)
        if not user_obj:
            messages.warning(request, 'Invalid password ')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        login(request , user_obj)
        return redirect('/',)

        
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return render(request ,'login.html')

def register_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username = username)

        if user_obj.exists():
            messages.warning(request, 'Username already exists')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        user = User.objects.create(username = username)
        user.set_password(password)
        user.save()
        return redirect('/')

    return render(request , 'register.html')


@login_required
def addContact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        phonenumber = request.POST.get('phonenumber')

        contact_obj = Contact.objects.filter(phonenumber=phonenumber)

        if contact_obj.exists():
            messages.warning(request, 'Phone number already exists')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        Contact.objects.create(created_by=request.user, name=name, address=address, phonenumber=phonenumber)
        messages.success(request, "Your contact has been saved")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    return render(request, 'addContact.html')

@login_required
def viewContact(request):
    contacts = Contact.objects.filter(created_by=request.user)
    return render(request, 'viewContact.html', {'contacts': contacts})


def logout_view(request):
    logout(request)
    return redirect('home') 
