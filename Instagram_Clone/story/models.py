from django.db import models
from shared.models import BaseModel

from users.models import UserModel

# --------------------------------------------------------------------------------
class StoryModel(BaseModel):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='stories')

    media = models.FieldFile(upload_to='stories')
    caption = models.CharField(max_length=255)
    expiry_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    

    def __str__(self):
        return self.caption
    
    class Meta:
        verbose_name = 'story'
        verbose_name_plural = 'stories'

# --------------------------------------------------------------------------------
class StoryViewModel(BaseModel):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='story-views')
    story = models.ForeignKey(StoryModel, on_delete=models.CASCADE, related_name='story-views')

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = 'StoryView'
        verbose_name_plural = 'StoryViews'


# --------------------------------------------------------------------------------
class StoryInteractionModel(BaseModel):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='story-views')
    story = models.ForeignKey(StoryModel, on_delete=models.CASCADE, related_name='story-views')

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = 'StoryView'
        verbose_name_plural = 'StoryViews'
