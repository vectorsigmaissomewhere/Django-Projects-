from django.contrib.auth.models import User
from django.db import models
import uuid

class BaseModel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True

class Contact(BaseModel):
    name = models.CharField(max_length=255)
    address = models.TextField()
    phonenumber = models.CharField(max_length=15)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contacts')

    def __str__(self) -> str:
        return self.name
