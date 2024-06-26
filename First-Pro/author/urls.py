from django.urls import path
from author.views import *


app_name = 'user'

urlpatterns = [
    path('', AuthorMainView.as_view()),
    path('<int:pk>/', AuthorMainView.as_view()),
    path('<int:pk>/update/', AuthorUpdateView.as_view()),
    path('create/', AuthorCreateView.as_view()),
    path('<int:pk>/delete/', AuthorDeleteView.as_view())

]
