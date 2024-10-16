## Database Configurations in Django 

SQLite3 
```text
Open settings.py
DATABASE = {
    'default':{
        'ENGINE':'django.db.backends.sqlite3',
        'NAME':os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

MYSQL Configuration 
```text 
- Install mysql in your system 
- You have to create your own database and user to config 
MySQL with Django.
- Open settings.py
DATABASE = {
    'default':{
        'ENGINE':'django.db.backends.mysql',
        'NAME':'database_name',
        'USER':'user_name',
        'PASSWORD':'password',
        'HOST':'localhost',
        'PORT':port_number
    }
}

DATABASE = {
    'default':{
        'ENGINE':'django.db.backends.mysql',
        'NAME':'mydb',
        'USER':'root',
        'PASSWORD':'',
        'HOST':'localhost',
        'PORT': 5555
    }
}
```

Oracle SQL Configuration 
```text 
- Install Oracle in your system 
- You have to create your own database and user 
to config Oracle with Django 
- Open settings.py 
DATABASE = {
    'default':{
        'ENGINE':'django.db.backends.oracle',
        'NAME':'database_name',
        'USER':'user_name',
        'PASSWORD':'password',
        'HOST':'localhost',
        'PORT':port_number, 
    }
}

Same goes for postgres

ENGINE':'django.db.backends.postgres'
```
