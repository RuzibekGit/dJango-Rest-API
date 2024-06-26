from django.urls import path
from books.views import get_data_books, get_book, update_book, create_book, delete_book, filter_by_books
from books.views_class_base import *


app_name = 'books'

# -------- for function based views -----------
# urlpatterns = [
#     path('', get_data_books),
#     path('<int:pk>/', get_book),
#     path('<int:pk>/update/', update_book),
#     path('create/', create_book),
#     path('<int:pk>/delete/', delete_book),
#     path('filter/', filter_by_books),

# ]


# --------- for class based views ------------
urlpatterns = [
    path('', GetAllBooks.as_view()),
    path('<int:pk>/', BookDetailView.as_view()),
    path('<int:pk>/update/', UpdateBookView.as_view()),
    path('create/', CreateBookView.as_view()),
    path('<int:pk>/delete/', DeleteBookView.as_view()),

]

urlpatterns += [path('filter/', filter_by_books)]