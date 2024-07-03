from django.contrib import admin
from users.models import UserModel, ConfirmationModel
# Register your models here.


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'email']

# hi their


@admin.register(ConfirmationModel)
class ConfirmationModelAdmin(admin.ModelAdmin):
    list_display = ['code']
