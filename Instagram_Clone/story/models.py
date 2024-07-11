from django.db import models
from shared.models import BaseModel

from users.models import UserModel


class StoryModel(BaseModel):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='stories')

    media = models.FieldFile(upload_to='stories')
    caption = models.CharField(max_length=255)
    expiry_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    

    def __str__(self):
        return self.user
    
    class Meta:
        verbose_name = 'story'
        verbose_name_plural = 'stories'
    