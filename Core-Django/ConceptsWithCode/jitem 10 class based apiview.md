Class Based APIView

about
```text
Rest framework provides and APIView class, which subclasses Django's View class.
Difference Between APIView classes and regular View classes:
- Requests passed to the handler method will be REST framework's Request instances, not Django's HttpRequest instances.
- Handler methods may return REST framework's Response, instead of Django's HttpResponse. The view will manage content negotiation and setting the correct renderer on the response.
- Any APIException exceptions will be caught and mediated into apprpriate responses.
- Incoming request will be authenticated and appropriate permission and/or throttle checks will be run before dispatching the request to the handler method.
```

About the code
```python
from rest_framework.views import APIView
class StudentAPI(APIView):
    def get(self,request, format = None):
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many = True)
        return Response(serializer.data)

    def post(self, request, format = None):
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'},status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
```
