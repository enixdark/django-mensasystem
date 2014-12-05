from django.contrib import admin
from message.models import Message
# Register your models here.
class MessageAdmin(admin.ModelAdmin):
    list_display = ['user','time','message']
    search_fields = ['user__username','time']

admin.site.register(Message,MessageAdmin)
