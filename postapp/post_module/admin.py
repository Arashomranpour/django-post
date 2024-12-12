from django.contrib import admin

# Register your models here.
from . import models
class postAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.post._meta.get_fields()]


admin.site.register(models.post,postAdmin)
