from django.contrib import admin

from fundare.users.models import CustomUser

# Register your models here.
admin.site.register(CustomUser)