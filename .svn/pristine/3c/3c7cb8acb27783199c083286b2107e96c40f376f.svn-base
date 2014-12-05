from django.contrib import admin
from timesheet.models import *
# Register your models here.

from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

@receiver(pre_delete, sender=TimeWorking)
def _TimeWorking_delete(sender, instance, **kwargs):
    try:
        usertimesheet = UserTimeSheet.objects.get(user = instance.user,working_date = instance.working_date)
        usertimesheet.special = False
        usertimesheet.save()
    except UserTimeSheet.DoesNotExist:
        pass



@receiver(pre_delete, sender=UserTimeSheet)
def _UserTimeSheet_delete(sender, instance, **kwargs):
    try:
        report = Report.objects.get(user = instance.user,month = instance.working_date.month)
        report.fines -= instance.fines
        report.save()
    except UserTimeSheet.DoesNotExist:
        pass


def make_payment(modeladmin, request, queryset):
    from datetime import date
    from dateutil import parser
    for user in queryset:
        if not user.payment:
            report = Report.objects.get(user=user.user,month=user.working_date.month)
            report.fines -= user.fines
            report.save()
    queryset.update(payment=True)
    make_payment.short_description = "Mark selected payment"

def make_unpayment(modeladmin, request, queryset):
    from datetime import date
    from dateutil import parser
    for user in queryset:
        if user.payment:
            report = Report.objects.get(user=user.user,month=user.working_date.month)
            report.fines += user.fines
            report.save()
    queryset.update(payment=False)
    make_payment.short_description = "Mark selected not payament"
    list_per_page = 15

class UserTimeSheetAdmin(admin.ModelAdmin):
    def get_working_date(self, obj):
        return obj.working_date.strftime("%d/%m/%Y")

    list_display = ['user','working_date','status','special','payment']
    search_fields = ['user__username','working_date','status','special']
    actions = [make_payment,make_unpayment]
    date_hierarchy = 'working_date'
    list_per_page = 15

class TimeWorkingAdmin(admin.ModelAdmin):
    list_display = ['user','working_date','state','note']
    search_fields = ['user__username','working_date']
    list_per_page = 15

class TimeSheetMoneyAdmin(admin.ModelAdmin):
    list_display = ['fines_company_late','fines_home_early','method','exp','note']
    list_per_page = 15


class TimeSheetAdmin(admin.ModelAdmin):

    def get_morning_time_start(self, obj):
        return obj.morning_time_start.strftime("%H:%M:%S")

    def get_morning_time_end(self, obj):
        return obj.morning_time_end.strftime("%H:%M:%S")

    def get_afternoon_time_start(self, obj):
        return obj.afternoon_time_start.strftime("%H:%M:%S")

    def get_afternoon_time_end(self, obj):
        return obj.afternoon_time_end.strftime("%H:%M:%S")
    list_per_page = 15
    list_display = ['get_morning_time_start','get_morning_time_end','get_afternoon_time_start','get_afternoon_time_end','note']

admin.site.register(TimeSheet,TimeSheetAdmin)
admin.site.register(TimeSheetMoney,TimeSheetMoneyAdmin)
admin.site.register(Report)
admin.site.register(TimeWorking,TimeWorkingAdmin)
admin.site.register(UserTimeSheet,UserTimeSheetAdmin)
# admin.site.register(Settings)

