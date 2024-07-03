## ViewSet

about
```text
Django REST Framework allows you to combine the logic for a set
of related views in a single class, called a ViewSet.

There are two main advantages of using a ViewSet over using a View class.
- Repeated logic can be combined into a single class.
- By using routers, we no longer need to deal woth wiring up the URL conf ourselves.
means router gives url
```

## Some classes

ViewSet Class

about
```text
A ViewSet class is simply a type of class-based View, that does not provide any method handlers such as get() or post(), and instead provides actions such as list() and create().
- list() -> Get All Records
- retrieve() -> Get Single Record
- create() -> Create/Insert Record
- update() -> Update Record Completely
- partial_update() -> Update Record Partially
- destroy() -> Delete Record
```

How to make ViewSet class
```python
from rest_framework import viewsets
class StudentViewSet(viewsets.ViewSet):
    def list(self, request): ................
    def create(self, request): .....................
    def retrieve(self, request, pk = None): ........................
    def update(self, request, pk = None): ..............
    def partial_update(self, request, pk = None): ................
    def destroy(self, request, pk = None): ....................
```
