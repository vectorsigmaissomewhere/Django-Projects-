## Here we will learn how to connect Django with react js 

## CRUD USING DJANGO REST FRAMEWORK AND REACT JS 

api/admin.py
```python
from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','stuname','email']
```

api/models.py
```python
from django.db import models

class Student(models.Model):
    stuname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
```

api/serializers.py
```python
from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','stuname','email']
```

api/urls.py
```python
from django.urls import path
from api import views

urlpatterns = [
    path('student/', views.StudentList.as_view(), name='student-list'),
    path('student/create/', views.StudentCreate.as_view(), name='student-create'),
    path('student/retrieve/<int:pk>/', views.StudentRetrieve.as_view(), name='student-retrieve'),
    path('student/update/<int:pk>/', views.StudentUpdate.as_view(), name='student-update'),
    path('student/delete/<int:pk>/', views.StudentDestroy.as_view(), name='student-delete'),
]
```

api/views.py
```python
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.generics import DestroyAPIView

from .models import Student

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentCreate(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieve(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentUpdate(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDestroy(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
```


djangobackend/settings.py
```python
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@wks#4%+39ekpq&o)!xaufetr2$%_^6px)o28l#p-njiz&ln=6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'api',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'djangobackend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'djangobackend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': ('rest_framework.renderers.JSONRenderer',)
}

CORS_ALLOWED_ORIGINS = [
    'http://localhost:5173', # this is the react port that is being running 
]

APPEND_SLASH=False
```

djangobackend/urls.py
```python
from django.urls import path
from api import views

urlpatterns = [
    path('student/', views.StudentList.as_view(), name='student-list'),
    path('student/create/', views.StudentCreate.as_view(), name='student-create'),
    path('student/retrieve/<int:pk>/', views.StudentRetrieve.as_view(), name='student-retrieve'),
    path('student/update/<int:pk>/', views.StudentUpdate.as_view(), name='student-update'),
    path('student/delete/<int:pk>/', views.StudentDestroy.as_view(), name='student-delete'),
]
```

pip freeze the requirements
```text
Django==5.0.6
django-cors-headers==4.4.0
djangorestframework==3.15.1
if you need more requirements you add it in your project
```



## These are the frontend code

App.jsx
```jsx
import { useState, useEffect } from "react";
import axios from "axios";

function App() {
  const [students, setStudents] = useState([]);
  // for put request
  const [editStudent, setEditStudent] = useState(null);
  const [editStudentname, setEditStudentname] = useState('');
  const [editStudentemail, setEditStudentemail] = useState('');
  // for post request
  const [postStudentName, setPostStudentName] = useState('');
  const [postStudentEmail, setPostStudentEmail] = useState(''); 
  // for retrieving student
  const [oneStudent, setOneStudent] = useState(null);

  const handleNameChange = (event) => {
    setPostStudentName(event.target.value);
  }

  const handleEmailChange = (event) => {
    setPostStudentEmail(event.target.value);
  }

  const handleSubmit = (event) => {
    event.preventDefault();
    const context = { stuname: postStudentName, email: postStudentEmail };
    axios.post('http://127.0.0.1:8000/api/student/create/', context)
      .then(response => {
        console.log('Student added:', response.data);
        alert(`Form submitted with input: ${postStudentName} ${postStudentEmail}`);
        setPostStudentName('');
        setPostStudentEmail('');
      })
      .catch(error => console.error('Error adding student:', error));
  }

  useEffect(() => {
    async function getAllStudent() {
      try {
        const response = await axios.get("http://127.0.0.1:8000/api/student/");
        console.log(response.data);
        setStudents(response.data);
      } catch (error) {
        console.log(error);
      }
    }
    getAllStudent();
  }, []);

  const deleteStudent = (id) => {
    axios.delete(`http://127.0.0.1:8000/api/student/delete/${id}/`)
      .then(() => {
        setStudents(students.filter(student => student.id !== id));
      })
      .catch(error => console.error('Error deleting data:', error));
  };

  const handleEditClick = (student) => {
    setEditStudent(student);
    setEditStudentname(student.stuname);
    setEditStudentemail(student.email);
  } 

  const handleUpdateSubmit = (e) => {
    e.preventDefault();
    const updatedStudent = { ...editStudent, stuname: editStudentname, email: editStudentemail };

    axios.put(`http://127.0.0.1:8000/api/student/update/${editStudent.id}/`, updatedStudent)
      .then(() => {
        setStudents(students.map(student =>
          student.id === editStudent.id ? updatedStudent : student
        ));
        setEditStudent(null);
        setEditStudentname('');
        setEditStudentemail('');
      })
      .catch(error => console.error('Error updating data:', error));
  }

  const viewStudent = (id) => {
    axios.get(`http://127.0.0.1:8000/api/student/retrieve/${id}/`)
      .then(response => {
        console.log('Student retrieved:', response.data);
        setOneStudent(response.data);
      })
      .catch(error => console.error('Error retrieving student:', error));
  }

  return (
    <>
      <div className="App">
        <h1>Connect React JS to Django</h1>
        {
          students.map((student, i) => {
            return (
              <h2 key={i}>{student.id} {student.stuname} {student.email}
                <button onClick={() => viewStudent(student.id)}>View More</button>
                <button onClick={() => deleteStudent(student.id)}>Delete</button>
                <button onClick={() => handleEditClick(student)}>Edit</button>
              </h2>
            );
          })
        }
        
        {editStudent && (
          <div>
            <h2>Edit Student</h2>
            <form onSubmit={handleUpdateSubmit}>
              <input
                type="text"
                placeholder="studentname"
                value={editStudentname}
                onChange={(e) => setEditStudentname(e.target.value)}
                required
              />
              <input
                type="email"
                placeholder="studentemail"
                value={editStudentemail}
                onChange={(e) => setEditStudentemail(e.target.value)}
                required
              />
              <button type="submit">Update</button>
              <button type="button" onClick={() => setEditStudent(null)}>Cancel</button>
            </form>
          </div>
        )}

        {oneStudent && (
          <div>
            <h2>Student Details</h2>
            <p>ID: {oneStudent.id}</p>
            <p>Name: {oneStudent.stuname}</p>
            <p>Email: {oneStudent.email}</p>
            <button onClick={() => setOneStudent(null)}>Close</button>
          </div>
        )}

        <h1>Add Students</h1>
        <form onSubmit={handleSubmit}>
          <label>Enter your Name</label>
          <input type="text" value={postStudentName} onChange={handleNameChange} />
          <label>Enter your Email</label>
          <input type="email" value={postStudentEmail} onChange={handleEmailChange} />
          <button type="submit">Submit</button>
        </form>
      </div>
    </>
  );
}

export default App;
```


Note: 
```text
- check your settings.py
CORS_ALLOWED_ORIGINS = [
    'http://localhost:5173', # this is the react port that is being running 
]
the port number your are seeing is your react js port

- add APPEND_SLASH=False
in your setting.py file add APPEND_SLASH = false


all the CRUD operation will be available at the end of the day 
```
