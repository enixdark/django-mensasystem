from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.


# #add a Inline in Edit of User Page
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    # can_delete = True
    verbose_name_plural = 'Userprofile'

class UserProfileAdmin(UserAdmin):
    inlines = (UserProfileInline, )
    search_fields = ('username',)
#
#
#
# # from django.contrib.auth.models import User
# #
# # class MyUserAdmin(UserAdmin):
# #     list_filter = UserAdmin.list_filter + ('is_active',)
# #
# # admin.site.unregister(User)
# # admin.site.register(User, MyUserAdmin)
# #register User again
admin.site.unregister(User)
admin.site.register(User,UserProfileAdmin)
# admin.site.register(Project)
# admin.site.register(ProjectUser)
# admin.site.register(Task)
# admin.site.register(Setting)
#
#
