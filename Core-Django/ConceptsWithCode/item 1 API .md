## api

 types of api 

```text
private api  - used within the organization
partner api  - used within business partner
public api  - that we use, developers
```

Example 1: integration of google map 
```text
my application can use the google map api
```

Example 2: want to show product from various wesbite
```text
To show product of their website product 
I will use their api to show the product in my website
``` 

Example 3: use of api for hybrid application
```text
web application 
		  ----
Mobile application           -----
                                                         ------- APi ------Web app -----Database
                                    ------
Ios application 
```

## How to use api 

```text
sign up to api
Need api key/token for authentication purpose
to communicate with server make request to api with api key
if api key authentication succeed api will provide required data
```


## Web api

```text
made for web app
request and response
```

```text
User <-->  web api   <--> web application  <--> database
```
How it works
```text
client send request to web api
if needed web api communicate to web application/database 
web app/database provides required data to api
api returns data to client
```

## Rest and Rest API

Rest 

```text
Architectural guideline to develop web api
```

Rest API

```text
API which is developed using REST is known as REST API/
RESTFUL API
```


Example 1

```text
Example 3: use of api for hybrid application
which is shown above
```


how rest api works

```text
works the same as web api
```

CRUD Operations - 
```text
look for http method
C POST
R GET
U PUT, PATCH
D DELETE
```

Students API Resouce
```text
http://googlebeta.com/api/students
Here is is giving us students
googlebeta.com -> base url
api -> Naming Convention / we make the name as api
students -> Resouce of api or end point of api
```

## Request  - Response
```text
request  -> GET 
Request for all students  -> Here Request will be Get:/api/students/
Response -> in json format , student detail
request for one student having id = 1
Reqest -> Get:/api/students/
or Request -> GET:/api/students/1

request -> POST
request -> POST:/api/students/data

request -> PUT to update max data
PUT or Patch :/api/students/1/data

request -> request for deleting data, id = 1
delete:/api/students/1/data
```
