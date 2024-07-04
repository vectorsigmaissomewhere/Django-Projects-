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

ViewSet CLass
```text
During dispatch, the following attributes are available on the ViewSet: -
- basename - the base to use for the URL names that are created.
- action - the name of the current action(e.g., list, create).
- detial - boolean indicating if the current action is configures for a list or detail
- suffix - the display suffix for the viewset type - mirrors the detail attribute
- name - the display name for the viewset. This argument is mutually exclusive to suffix.
- description - the display description for the individual view of a viewset.
```

ViewSet - URL Config
```python 
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter() # creating default router object
router.register('studentapi', views.StudentViewSet, basename = 'student') # register StudentViewSet with Router
urlpatterns = [
    path('', include(router.urls)), # The API URLS are now determined automatically by the router
]
```
