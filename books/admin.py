from django.contrib import admin
from books.models import BooksModel

# Register your models here.


@admin.register(BooksModel)
class BooksAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'subtitle']
