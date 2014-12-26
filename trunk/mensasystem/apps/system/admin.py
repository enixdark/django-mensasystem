from django.contrib import admin
from .models import *
# Register your models here.

class SystemAdmin(admin.ModelAdmin):
    list_display = ['ip']

admin.site.register(SystemIP,SystemAdmin)