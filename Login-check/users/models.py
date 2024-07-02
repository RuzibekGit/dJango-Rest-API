from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class BaseModel(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserModel(AbstractUser, BaseModel):
    
    email        = models.EmailField(null=True, blank=True)
    avatar       = models.ImageField(null=True, blank=True, upload_to='avatars')
    bio          = models.TextField (null=True, blank=True)

    # --------------- Functions -----------------
    def __str__(self): return self.get_full_name()