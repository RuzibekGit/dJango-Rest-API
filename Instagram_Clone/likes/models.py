from django.db import models

from users.models import UserModel
from posts.models import PostModel
from comments.models import CommentsModel
from users.models import BaseModel





# ------------------  Model -----------------------
# region post
class LikesModel(BaseModel):
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='post_likes')

    # TODO: Add functionality so that users can like the comment as well.
    # comments = models.ForeignKey(CommentsModel, on_delete=models.CASCADE, related_name='likes', null=True, blank=True)
    def __str__(self):
        return self.user.full_name

    class Meta:
        db_table = 'post_likes'
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'
# endregion
