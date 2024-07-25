About it
```text
Doing jwt authentication with react js
```

About the Project Folder
```text
app name : account
project name : jwtauthentication
```

account/admin.py
```python
from django.contrib import admin
from account.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class UserModelAdmin(BaseUserAdmin):
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserModelAdmin
    # that reference specific fields on auth.User.
    list_display = ["id","email", "name","tc","is_admin"]
    list_filter = ["is_admin"]
    fieldsets = [
        ("User Credentials", {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["name", "tc"]}),
        ("Permissions", {"fields": ["is_admin"]}),
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserModelAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "name","tc", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email", "id"]
    filter_horizontal = []


# Now register the new UserModelAdmin...
admin.site.register(User, UserModelAdmin)
```

account/apps.py
```python
from django.apps import AppConfig


class AccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'account'
```

account/models.py
```python
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Custom User Manager
class UserManager(BaseUserManager):
    def create_user(self, email, name, tc, password=None, password2=None):
        """
        Creates and saves a User with the given email,name, tc and password
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            tc=tc,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, tc, password=None):
        """
        Creates and saves a superuser with the given email ,name, tc and password.
        """
        user = self.create_user(
            email,
            password=password,
            name = name,
            tc = tc,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
    
# Custom User Model
class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="Email",
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=200)
    tc = models.BooleanField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name","tc"]

    def __str__(self): # objects being show by email
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
```

account/renderers.py
```python
from rest_framework import renderers
import json

# this is mentioned in settings.py
class UserRenderer(renderers.JSONRenderer):
    charset = 'utf-8'
    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = ''
        if 'ErrorDetail' in str(data):
            response = json.dumps({'errors':data})
        else:
            response = json.dumps(data)
        return response
```

account/serializers.py
```python
from rest_framework import serializers
from account.models import User
from xml.dom import ValidationErr
from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
# from utils import Util

class UserRegistrationSerializer(serializers.ModelSerializer):
    # We are writing this because we need  confirm password field is in our Registration Request
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = User
        fields = ['email','name','password','password2','tc']
        extra_kwargs = {
            'password':{'write_only':True}
        }
    
    # Validating Password and Confirm Password while Registration
    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError("Password and Confirm Password doesn't match")
        return attrs
    
    def create(self, validate_data):
        return User.objects.create_user(**validate_data)
    

class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = User
        fields = ['email', 'password']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email','name']

class UserChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
    password2 = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
    class Meta:
        fields = ['password','password2']
    
    def validate(self,attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        user = self.context.get('user')
        if password != password2:
            raise serializers.ValidationError("Password and Confirm Password doesn't match")
        user.set_password(password)
        user.save()
        return attrs

# send email to user
class SendPasswordResetEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        fields = ['email']
    
    def validate(self, attrs):
        email = attrs.get('email')
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uid = urlsafe_base64_encode(force_bytes(user.id)) # this method only takes in byte so force_bytes converts into bytes
            print('Encoded UID', uid)
            token = PasswordResetTokenGenerator().make_token(user) # makes one token
            print('Password Reset Token', token)
            link = 'http://localhost:8000/api/user/reset/'+uid+'/'+token
            print('Password Rest Link',link)
            # SEND EMAIL CODE 
            """
            body = 'Click Following Link to Reset Your Password'+link
            data = {
                'subject':'Reset Your Password',
                'body':body,
                'to_email':user.email
            }
            Util.send_email(data)
            """
            return attrs
        else:
            raise ValidationErr('YOu are not a Registered User')
        
# Creating serializer for UserPasswordResetSerializer
class UserPasswordResetSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
    password2 = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
    class Meta:
        fields = ['password','password2']
    
    def validate(self,attrs):
        try:
            password = attrs.get('password')
            password2 = attrs.get('password2')
            uid = self.context.get('uid')
            token = self.context.get('token')
            if password != password2:
                raise serializers.ValidationError("Password and Confirm Password doesn't match")
            id = smart_str(urlsafe_base64_decode(uid)) # smart_str converts into string
            user = User.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                raise ValidationErr('Token is not Valid or Expired')
            user.set_password(password)
            user.save()
            return attrs
        except DjangoUnicodeDecodeError as identifier:
            PasswordResetTokenGenerator().check_token(user, token)
            raise ValidationErr('Token is not Valid or Expired')
```

account/urls.py
```python
from django.urls import path, include
from account.views import UserRegistrationView, UserLoginView, UserProfileView, UserChangePasswordView, SendPasswordResetEmailView, UserPasswordResetView

urlpatterns = [
    path('register/',UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('changepassword/', UserChangePasswordView.as_view(), name='changepassword'),
    path('send-reset-password-email/', SendPasswordResetEmailView.as_view(), name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset-password')
]
```

account/views.py
```python
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from account.serializers import UserRegistrationSerializer, UserLoginSerializer, UserProfileSerializer, UserChangePasswordSerializer, SendPasswordResetEmailSerializer, UserPasswordResetSerializer
from django.contrib.auth import authenticate
from account.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken # generate token
from rest_framework.permissions import IsAuthenticated


# Generate Token Manually
def get_token_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class UserRegistrationView(APIView):
    renderer_classes = [UserRenderer] # will show the error that your have provided
    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token = get_token_for_user(user)
            return Response({'token':token, 'msg':'Registration Successful'},status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserLoginView(APIView):
    renderer_classes = [UserRenderer] # will show the error that your have provided
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                token = get_token_for_user(user)
                return Response({'token':token, 'msg':'Login Success'}, status=status.HTTP_200_OK)
            else:
                return Response({'errors':{'non_field_errors':['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserProfileView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserChangePasswordView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def post(self,request, format=None):
        serializer = UserChangePasswordSerializer(data=request.data,context={'user':request.user})
        if serializer.is_valid(raise_exception=True):
            return Response({'msg':'Password Changed Successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
# send email to user for password change
class SendPasswordResetEmailView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format=None):
        serializer = SendPasswordResetEmailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response({'msg':'Password Reset link send. Please check your Email'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# update the password now
class UserPasswordResetView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, uid, token, format=None):
        serializer = UserPasswordResetSerializer(data=request.data, context={'uid':uid, 'token': token})
        if serializer.is_valid(raise_exception=True):
            return Response({'msg':'Password Reset Successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

jwtauthentication/settings.py
```python
from pathlib import Path
from datetime import timedelta
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!3h(=&v_)(wx4os9dt1k6#-q+%-r%(2_r_$!u(14%^^=g*)_zg'

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
    'account',
    'rest_framework',
    'corsheaders'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'jwtauthentication.urls'

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

WSGI_APPLICATION = 'jwtauthentication.wsgi.application'


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

 # select User model which is in account
AUTH_USER_MODEL = 'account.User'

# cors to avoid conflict with react js
CORS_ALLOWED_ORIGINS = [
    'http://localhost:5173',# front end url
]



REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES':(
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    #'DEFAULT_RENDERER_CLASSES':('rest_framework.renderers.JSONRenderer',) # removing browsable api
    
}

# SIMPLE JWT AUTHENTICATION
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=20),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),

    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",

    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",

    "JTI_CLAIM": "jti",

    "TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainPairSerializer",
    "TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSerializer",
    "TOKEN_VERIFY_SERIALIZER": "rest_framework_simplejwt.serializers.TokenVerifySerializer",
    "TOKEN_BLACKLIST_SERIALIZER": "rest_framework_simplejwt.serializers.TokenBlacklistSerializer",
    "SLIDING_TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainSlidingSerializer",
    "SLIDING_TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSlidingSerializer",
}

# PASSWORD RESET TOKEN TIMEOUT
PASSWORD_RESET_TIMEOUT=900      # 900 Sec = 15min

# EMAIL CONFIGURATION
"""
EMAIL_BACKEND="django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587
EMAIL_HOST_USER = os.environ.get('EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_USER')
EMAIL_USE_TLS = True
"""
```

urls.py
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('account.urls'))
]
```

manage.py
```python
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import dotenv

def main():
    """Run administrative tasks."""
    # dotenv.read_dotenv()
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jwtauthentication.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
```

requirements
```text
Django==5.0.6
django-cors-headers==4.4.0
django-dotenv==1.4.2
djangorestframework==3.15.1
djangorestframework-simplejwt==5.3.1
```
Note
```text
You cannot change the password without knowing the password
As Google doesn't allow to let third party application to help in change password(something like that)
```
## Frontend code

components/Footer.jsx
```jsx
import React from 'react';

const Footer = () => {
  return <footer><h1>Footer</h1></footer>;
}

export default Footer;
```

components/Header.jsx
```jsx
import React from 'react';
import { Link } from 'react-router-dom';

const Header = () => {
  return (
    <header>
      <h1>Header</h1>
      <nav>
        <Link to="/">Home</Link>
        <Link to="/register">Register</Link>
      </nav>
    </header>
  );
}

export default Header;
```

components/Register.jsx
```jsx
import React, { useState } from 'react';
import axios from 'axios';

const Register = () => {
  const [email, setEmail] = useState('');
  const [name, setName] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [tc, setTc] = useState(true);
  const [message, setMessage] = useState('');
  const [errors, setErrors] = useState({});

  const handleSubmit = (e) => {
    e.preventDefault();
    if (password !== confirmPassword) {
      setMessage('Passwords do not match');
      return;
    }

    const newUser = {
      email,
      name,
      password,
      password2: confirmPassword,
      tc: tc.toString() 
    };

    axios.post('http://127.0.0.1:8000/api/user/register/', newUser)
      .then(response => {
        setEmail('');
        setName('');
        setPassword('');
        setConfirmPassword('');
        setTc(true);
        setMessage('Registration Successful');
        setErrors({});
        console.log('User registered successfully:', response.data);
      })
      .catch(error => {
        console.error('Error adding data:', error);
        setMessage('Registration failed. Please try again.');
        if (error.response && error.response.data) {
          setErrors(error.response.data);
        }
      });
  };

  return (
    <div className='contact'>
      <main>
        <h1>Contact Us</h1>
        {message && <p>{message}</p>}
        {errors && <ul>
          {Object.keys(errors).map((key, index) => (
            <li key={index}>{`${key}: ${errors[key]}`}</li>
          ))}
        </ul>}
        <form onSubmit={handleSubmit}>
          <div>
            <label htmlFor='email'>Email</label>
            <input
              type='email'
              id='email'
              required
              placeholder='Abc@xyz.com'
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />
          </div>
          <div>
            <label htmlFor='name'>Name</label>
            <input
              type='text'
              id='name'
              required
              placeholder='Abc'
              value={name}
              onChange={(e) => setName(e.target.value)}
            />
          </div>
          <div>
            <label htmlFor='password'>Password</label>
            <input
              type='password'
              id='password'
              required
              placeholder='Password'
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
          </div>
          <div>
            <label htmlFor='confirmPassword'>Confirm Password</label>
            <input
              type='password'
              id='confirmPassword'
              required
              placeholder='Confirm Password'
              value={confirmPassword}
              onChange={(e) => setConfirmPassword(e.target.value)}
            />
          </div>
          <div>
            <label htmlFor='tc'>Terms and Conditions</label>
            <input
              type='checkbox'
              id='tc'
              checked={tc}
              onChange={() => setTc(!tc)}
            />
          </div>
          <button type='submit'>Send</button>
        </form>
      </main>
    </div>
  );
}

export default Register;
```

Login.jsx
```jsx
import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const Login = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState('');
  const [errors, setErrors] = useState({});
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();

    const userCredentials = { email, password };

    axios.post('http://127.0.0.1:8000/api/user/login/', userCredentials)
      .then(response => {
        setEmail('');
        setPassword('');
        setMessage('Login Successful');
        setErrors({});

        // Store tokens in localStorage
        localStorage.setItem('refreshToken', response.data.token.refresh);
        localStorage.setItem('accessToken', response.data.token.access);

        // Redirect to profile or other protected page
        navigate('/profile');
      })
      .catch(error => {
        console.error('Error logging in:', error);
        setMessage('Login failed. Please try again.');
        if (error.response && error.response.data) {
          setErrors(error.response.data);
        }
      });
  };

  return (
    <div className='login'>
      <main>
        <h1>Login</h1>
        {message && <p>{message}</p>}
        {errors && <ul>
          {Object.keys(errors).map((key, index) => (
            <li key={index}>{`${key}: ${errors[key]}`}</li>
          ))}
        </ul>}
        <form onSubmit={handleSubmit}>
          <div>
            <label htmlFor='email'>Email</label>
            <input
              type='email'
              id='email'
              required
              placeholder='Abc@xyz.com'
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />
          </div>
          <div>
            <label htmlFor='password'>Password</label>
            <input
              type='password'
              id='password'
              required
              placeholder='Password'
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
          </div>
          <button type='submit'>Login</button>
        </form>
      </main>
    </div>
  );
}

export default Login;
```

Profile.jsx
```jsx
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const Profile = () => {
  const [profile, setProfile] = useState(null);
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();

  useEffect(() => {
    const token = localStorage.getItem('accessToken');

    if (!token) {
      navigate('/login'); // Redirect to login if no token
      return;
    }

    axios.get('http://127.0.0.1:8000/api/user/profile/', {
      headers: {
        Authorization: `Bearer ${token}`
      }
    })
    .then(response => {
      setProfile(response.data);
      setLoading(false);
      setError('');
    })
    .catch(error => {
      console.error('Error fetching profile:', error);
      setError('Failed to load profile.');
      setLoading(false);
    });
  }, [navigate]);

  if (loading) return <p>Loading profile...</p>;

  return (
    <div className='profile'>
      <main>
        <h1>User Profile</h1>
        {error && <p>{error}</p>}
        {profile ? (
          <div>
            <p><strong>ID:</strong> {profile.id}</p>
            <p><strong>Email:</strong> {profile.email}</p>
            <p><strong>Name:</strong> {profile.name}</p>
          </div>
        ) : (
          <p>No profile data available.</p>
        )}
      </main>
    </div>
  );
}

export default Profile;
```

ChangePassword.jsx
```jsx
import React, { useState } from 'react';
import axios from 'axios';

const ChangePassword = () => {
  const [password, setPassword] = useState('');
  const [password2, setPassword2] = useState('');
  const [message, setMessage] = useState('');
  const [errors, setErrors] = useState({});
  const [loading, setLoading] = useState(false);

  const handleSubmit = (e) => {
    e.preventDefault();
    setLoading(true);

    const passwordData = { password, password2 };

    axios.post('http://127.0.0.1:8000/api/user/changepassword/', passwordData, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('accessToken')}`
      }
    })
      .then(response => {
        setPassword('');
        setPassword2('');
        setMessage(response.data.msg || 'Password changed successfully!');
        setErrors({});
      })
      .catch(error => {
        console.error('Error changing password:', error);
        setMessage('Failed to change password. Please try again.');
        if (error.response && error.response.data) {
          setErrors(error.response.data);
        }
      })
      .finally(() => {
        setLoading(false);
      });
  };

  return (
    <div className='change-password'>
      <main>
        <h1>Change Password</h1>
        {message && <p>{message}</p>}
        {errors && <ul>
          {Object.keys(errors).map((key, index) => (
            <li key={index}>{`${key}: ${errors[key]}`}</li>
          ))}
        </ul>}
        <form onSubmit={handleSubmit}>
          <div>
            <label htmlFor='password'>New Password</label>
            <input
              type='password'
              id='password'
              required
              placeholder='Enter new password'
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
          </div>
          <div>
            <label htmlFor='password2'>Confirm Password</label>
            <input
              type='password'
              id='password2'
              required
              placeholder='Confirm new password'
              value={password2}
              onChange={(e) => setPassword2(e.target.value)}
            />
          </div>
          <button type='submit' disabled={loading}>
            {loading ? 'Changing Password...' : 'Change Password'}
          </button>
        </form>
      </main>
    </div>
  );
};

export default ChangePassword;
```

App.jsx
```jsx
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Register from './components/Register';
import Login from './components/Login';
import Profile from './components/Profile';
import Header from './components/Header'; 
import Footer from './components/Footer'; 
import ChangePassword from './components/ChangePassword'; 

function App() {
  return (
    <>
      <Router>
        <Header />
        <Routes>
          <Route path="/register" element={<Register />} />
          <Route path="/login" element={<Login />} />
          <Route path="/profile" element={<Profile />} />
          <Route path="/changepassword" element={<ChangePassword />} />
          <Route path="/" element={<h1>Welcome to the App</h1>} />
        </Routes>
        <Footer />
      </Router>
    </>
  );
}

export default App;
```

main.jsx
```jsx
import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)
```


## Testing in POSTMAN API

1 Check the user profile
![See the user profile](https://github.com/vectorsigmaissomewhere/Django-Projects-/blob/main/SomeImages/checking%20userprofile.PNG)

2 Change your password
![Change your password part 1](https://github.com/vectorsigmaissomewhere/Django-Projects-/blob/main/SomeImages/passwordchangepart1.PNG)
![Change your password part 2](https://github.com/vectorsigmaissomewhere/Django-Projects-/blob/main/SomeImages/passwordchangepart2.PNG)

3 Change your password with email
![Change password with email part 1](https://github.com/vectorsigmaissomewhere/Django-Projects-/blob/main/SomeImages/sendpasswordresetemailpart1.PNG)
![Change password with email part2](https://github.com/vectorsigmaissomewhere/Django-Projects-/blob/main/SomeImages/sendpasswordresetemailpart2.PNG)
