from django.db import models

from users.models import UserModel
from posts.models import PostsModel



class CommentsModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='comments')
    
    post = models.ForeignKey(PostsModel, on_delete=models.CASCADE, related_name="comments", null=True, blank=True)
    # comment_to_comment = models.ForeignKey(CommentsModel, on_delete=models.CASCADE, null=True, blank=True)
    
    comment = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  

    def __str__(self) -> str:
        return self.comment  

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
