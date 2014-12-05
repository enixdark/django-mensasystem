from django.contrib import admin
from system.models import *
# Register your models here.

class SystemAdmin(admin.ModelAdmin):
    list_display = ['start_ip','end_ip']

admin.site.register(SystemIP,SystemAdmin)