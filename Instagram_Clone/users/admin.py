from users.models import UserModel, ConfirmationModel
from django.contrib import admin



@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'user_role', 'phone_number']

# hi their

@admin.register(ConfirmationModel)
class ConfirmationModelAdmin(admin.ModelAdmin):
    list_display = ['code']
