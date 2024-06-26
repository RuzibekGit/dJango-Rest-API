from django.db import models

from users.models import UserModel
from posts.models import PostsModel
from comments.models import CommentsModel



class LikesModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='likes')

    post = models.ForeignKey(PostsModel, on_delete=models.CASCADE, related_name='likes', null=True, blank=True)
    comments = models.ForeignKey(CommentsModel, on_delete=models.CASCADE, related_name='likes', null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  

    def __str__(self) -> str:
        return self.comment  

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
