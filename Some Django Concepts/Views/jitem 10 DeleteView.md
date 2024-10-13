## Generic Editing View
```text
The following views are described on this page and provide a foundation for editing content:
- FormView
- CreateView
- UpdateView 
- DeleteView
```

DeleteView
```text
django.views.generic.edit.DeleteView

A view that displays a confirmation page and deletes an existing object. The given object 
will only be deleted if the request method is POST. If this view is fetched via GET, it 
will display a confirmation page that should contain a form that POSTs to the same URL.

This view inherits methods and attributes from the following views:
- django.views.generic.detail.SingleObjectTemplateResponseMixin
- django.views.generic.base.TemplateResponseMixin
- django.views.generic.edit.BaseDeleteView
- django.views.generic.edit.DeletionMixin
- django.views.generic.detail.BaseDetailView
- django.views.generic.detail.SingleObjectMixin 

Attribute:- 
template_name_suffix - The DeleteView page displayed to a GET request uses a 
template_name_suffixof'_confirm_delete'.

django.views.generic.edit.DeletionMixin
Enables handling of the DELETE http action.

Attributes:- 
success_url - The url to redirect to when the nominated object has been successfully 
deleted.
success_url may contain dictionary string formatting, which will be interpolated against
the object's filed attributes. For example, you could use success_url="/parent/{parent_id}/"
to redirect to a URL composed out of the parent_id field on a model.

Methods:- 
delete(request, *args, **kwargs) - Retireves the target object and calls its delete() 
method, then redirects to the success URL.

get_success_url() - Returns the url to redirect to when the nominated object has been 
successfully deleted. Returns success_url by default.
```

## Coding Part

```text
The other code file are similar to other updateview
```

deleteview/urls.py
```python
from django.contrib import admin
from django.urls import path
from school import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', views.StudentCreateView.as_view(), name='stucreate'),
    path('thanks/', views.ThanksTemplateView.as_view(), name='thankyou'),
    path('update/<int:pk>', views.StudentUpdateView.as_view(), name='stuupdate'),
    path('thanksupdate/', views.ThanksUpdateView.as_view(), name='thanksupdate'),
    path('create2/', views.StudentCreateView2.as_view(), name='stucreate2'),
    path('update2/<int:pk>', views.StudentUpdateView2.as_view(), name='stuupdate2'),
    path('delete/<int:pk>', views.StudentDeleteView.as_view(), name='studelete'),
    path('delete2/<int:pk>', views.StudentCustomDeleteView.as_view(), name='cusstudelete'),
]
```

school/templates/school/studel.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Do you want to delete?</h1>
    <form action="" method="post">
        {% csrf_token %}
        <input type="submit" value="Delete">
        <a href="{% url 'stucreate' %}">Cancel</a>
    </form>
</body>
</html>
```

school/templates/school/student_confirm_delete.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Do you want to delete?</h1>
    <form action="" method="post">
        {% csrf_token %}
        <input type="submit" value="Delete">
        <a href="{% url 'stucreate' %}">Cancel</a>
    </form>
</body>
</html>
```
check only delete view

school/views.py
```python
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from .models import Student 
from django.views.generic.base import TemplateView 
from django import forms

from .forms import StudentForm

"""Not working with forms.py"""
# Create your views here.
class StudentCreateView(CreateView):
    model = Student 
    fields = ['name', 'email', 'password']
    success_url = '/thanks/'
    template_name = 'school/student_form.html'

    # adding classes in form 
    def get_form(self):
        form = super().get_form()
        form.fields['name'].widget = forms.TextInput(attrs={'class':'myclass'})
        form.fields['password'].widget = forms.PasswordInput(attrs={'class':'mypass'})
        return form 


class ThanksTemplateView(TemplateView):
    template_name = 'school/thanks.html'

class StudentUpdateView(UpdateView):
    model = Student 
    fields = ['name', 'email', 'password']
    success_url = '/thanksupdate/'

    # adding classes in form 
    def get_form(self):
        form = super().get_form()
        form.fields['name'].widget = forms.TextInput(attrs={'class':'myclass'})
        form.fields['password'].widget = forms.PasswordInput(attrs={'class':'mypass'})
        return form 

class ThanksUpdateView(TemplateView):
    template_name = 'school/thanksupdate.html'



"""Now working with forms.py"""
class StudentCreateView2(CreateView):
    form_class = StudentForm 
    template_name = 'school/student_form.html'
    success_url = '/thanks/'

class StudentUpdateView2(UpdateView):
    model = Student
    form_class = StudentForm 
    template_name = 'school/student_form.html'
    success_url = '/thanksupdate/'


class StudentDeleteView(DeleteView):
    model = Student 
    success_url = '/create/'

# Delete with customtemplate
class StudentCustomDeleteView(DeleteView):
    model = Student 
    success_url = '/create/'
    template_name = 'school/studel.html'
```

Where to find the full code 
```text
check deleteview
```

What we can learn here
```text
To delete you will first get delete confirmation and then only the model object gets delete
after model object deletion the page will get rendered into create page and also
if you don't want to delete the page will get rendered into create page
```


