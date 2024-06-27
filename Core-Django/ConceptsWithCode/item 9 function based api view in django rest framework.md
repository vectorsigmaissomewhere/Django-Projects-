# Function Based api_view
about
```text
This wrapper provides a few bits of functionality such as making sure you receive Request
instances in your view, and adding context to Response objects so that content negotiation can be 
performed.
The wrapper also provides behaviour such as returning 405 Method Not Allowed reponses when appropriate, and handling and ParseError expections that occur when accessing request.data with malformed input.

By default only GET methods will be accepted. Other methods will respond with "405 Method
Not Allowed".

@api_view() then get is already present
but if you want get, post, put, delete what you can do to mention this is by 
@api_view(['GET','POST','PUT','DELETE'])
def function_name(request)
```

How to do this api_view
```text
- for get request
from rest_framework.decorators import api_view
from rest_framework.response import Response
@api_view(['GET'])
def student_list(request):
    if request.method == 'GET':
        stu  = Student.objects.all()
        serializer = StudentSerializer(stu,many = True)
        return Response(serializer.data)

```
