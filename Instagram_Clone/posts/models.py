from shared.models import BaseModel
from django.db import models

from users.models import UserModel



# class TagsModel(models.Model):  # TODO: 
#     name = models.CharField(max_length=122)

#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self) -> str:
#         return self.name
    
#     class Meta:
#         verbose_name = "Tag"
#         verbose_name_plural = "tags"



# ------------------ Post Model -----------------------
# region post
class PostModel(BaseModel):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='posts')

    image = models.ImageField(upload_to='posts')
    caption = models.TextField(null=True, blank=True)

#     TODO: adding functionality
#     location = models.CharField(max_length=122)
#     tags     = models.ManyToManyField(TagsModel, related_name='tags')
#     tag_user = models.ManyToManyField(UserModel, related_name='tags')  # tag yor friend

    def __str__(self):
        return self.caption

    class Meta:
        ordering = ['created_at']
        db_table = 'posts'
        verbose_name = 'post'
        verbose_name_plural = 'posts'
# endregion





