## Here we will learn how to connect Django with react js 

## Django Code 

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
    path('student/', views.StudentList.as_view()),
]
```

api/views.py
```python
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from .models import Student

class StudentList(ListAPIView):
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
```

djangobackend/urls.py
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('api.urls'))
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

  return (
    <>
      <div className="App">
        <h1>Connect React JS to Django</h1>
        {
          students.map((student, i) => {
            return (
              <h2 key={i}>{student.id} {student.stuname} {student.email}
                <button onClick={() => deleteStudent(student.id)}>Delete</button>
              </h2>
            );
          })
        }
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
```
