from django.contrib import admin

from fundare.users.models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'username']

admin.site.register(CustomUser)