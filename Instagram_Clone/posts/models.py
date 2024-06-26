from django.db import models

from users.models import UserModel



class TagsModel(models.Model):
    name = models.CharField(max_length=122)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "tags"


class PostsModel(models.Model):

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='posts')

    name  = models.CharField(max_length=256)
    image = models.ImageField(upload_to='posts')

    location = models.CharField(max_length=122)
    tags     = models.ManyToManyField(TagsModel, related_name='tags')
    tag_user = models.ManyToManyField(UserModel, related_name='tags')  # tag yor friend

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_created=True)


    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name ='Post'
        verbose_name_plural ='Posts'