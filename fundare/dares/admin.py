from django.contrib import admin
from .models import Charity, Dares, Dollars

# Register your models here.
class DaresAdmin(admin.ModelAdmin):
    list_filter = ("owner", "is_open",)
    list_display = ("title", "dare_description", "goal", "image", "date_created",)


class DollarsAdmin(admin.ModelAdmin):
    list_display = ("amount", "comment", "anonymous", "supporter",)
    list_filter = ("dares_id", "anonymous",)

admin.site.register(Charity)
admin.site.register(Dares, DaresAdmin)
admin.site.register(Dollars, DollarsAdmin)
