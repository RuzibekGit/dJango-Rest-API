from django.db import models

from users.models import UserModel, BaseModel
from posts.models import PostModel


# -------------------------- Comment -------------------------------
# region comment
class CommentsModel(BaseModel):
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='post_comments')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='child', null=True, blank=True)
    comment = models.TextField()

    def __str__(self):
        return self.comment

    class Meta:
        db_table = 'post_comments'
        verbose_name = 'post comment'
        verbose_name_plural = 'post comments'
# endregion

# -------------------------- Comment Like -------------------------------
# region comment like
class CommentLikeModel(BaseModel):
    comment = models.ForeignKey(CommentsModel, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='comment_likes')

    def __str__(self):
        return self.comment.comment

    class Meta:
        db_table = 'comment_likes'
        verbose_name = 'comment like'
        verbose_name_plural = 'comment likes'
# endregion
