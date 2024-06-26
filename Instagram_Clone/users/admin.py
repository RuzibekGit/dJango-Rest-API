from django.contrib import admin
from users.models import UserModel



@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'user_role', 'phone_number']

# hi their