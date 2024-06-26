from django.contrib import admin
from author.models import AuthorModel

# Register your models here.


@admin.register(AuthorModel)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'age', 'email', 'created_at']
