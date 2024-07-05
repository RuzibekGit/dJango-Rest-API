from django.contrib import admin

from posts.models import PostModel
from comments.models import CommentLikeModel, CommentsModel
from likes.models import LikesModel


@admin.register(PostModel)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'caption', 'user', 'created_at']
    search_fields = ['caption', 'user', 'id']
    list_filter = ['created_at', 'updated_at']


@admin.register(CommentsModel)
class PostCommentModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'comment', 'user', 'created_at']
    search_fields = ['comment', 'id']
    list_filter = ['created_at', 'updated_at']


@admin.register(LikesModel)
class PostLikeModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'user', 'created_at']
    search_fields = ['id']
    list_filter = ['created_at', 'updated_at']


@admin.register(CommentLikeModel)
class CommentLikeModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'comment', 'user', 'created_at']
    search_fields = ['id']
    list_filter = ['created_at', 'updated_at']
