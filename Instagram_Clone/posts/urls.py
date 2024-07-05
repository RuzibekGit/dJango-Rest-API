from django.urls import path

from posts.views import PostListView,  PostCreateView

app_name = 'posts'

urlpatterns = [
    path('', PostListView.as_view(), name='list'),
    path('create/', PostCreateView.as_view(), name='create'),
    
]
