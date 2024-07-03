from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from datetime import timedelta

import uuid

NEW, CODE_VERIFIED, DONE = "NEW", "CODE_VERIFIED", "DONE"

class BaseModel(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserModel(AbstractUser, BaseModel):
    
    AUTH_STATUSES = (
        (NEW, NEW),
        (CODE_VERIFIED, CODE_VERIFIED),
        (DONE, DONE),
    )
    
    email        = models.EmailField(null=True, blank=True)
    bio          = models.TextField (null=True, blank=True)

    auth_status = models.CharField(max_length=128, choices=AUTH_STATUSES, default=NEW)


    # --------------- Functions -----------------
    def __str__(self): return self.get_full_name()
    

# -------------------------- Confirmation -------------------------------
# region confirmation
class ConfirmationModel(models.Model):

    user            = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='verification_codes')
    expiration_time = models.DateField()
    is_confirmed    = models.BooleanField(default=False)
    code            = models.CharField(max_length=8, null=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.expiration_time = timezone.now() + timedelta(minutes=5)


# endregion