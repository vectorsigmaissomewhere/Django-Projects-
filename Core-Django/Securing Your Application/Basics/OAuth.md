## OAuth authentication Using Google Sign-in

what are the things we need to set up
```text
key and secret key of google or 
if you are using any other provider 
you need to use the provider key and secret key
```

Set up the project
```text
pip install django
django-admin startproject googlelogin
create a new app called users
```

More setup
```text
google cloud console
click on project
create a new project
call it django-tutorial

now select the project
now expand the naviation menu which is on the left hand side
click on or hover api and services 
and then select OAuth consent screen
now select on external
and then click on create
then fill all the crendentials
in my case I will name the app name as Django-Tutorial
fill the email
just leave other info 
but fill the developer contact information
and save and continue 

===============SCOPE PAGE=======================
click on add or removes copes button
so now just select the email and userinfo.profile
and click on update
save and continue and move on to next page

================TEST USERS====================
don't need to do it
just save and continue

================SUMMARY====================
back to dashboard


now you are on your dashboard
Click on the credentials which is on the left side
now on the top click on create credentials
select OAuth client ID
there you need to select Web application as the application type
now then give it a name as Django
You don't have to fill the authorized Javascript origins for now 
go take a look to authorized redirect URls
there click on to Add URLs
http://127.0.0.1:8000
second url 
http://127.0.0.1:8000/accounts/google/login/callback
and then click on create

Now what we need is a client ID and a client secret key
you can even download the json file
```


## Coding part
