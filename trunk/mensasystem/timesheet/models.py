from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.db.models import Q
# Create your models here.
from datetime import date
from django.forms.fields import ChoiceField


class TimeSheetManager(models.Manager):


    def getTimeSheetForUser(self):
        return super(TimeSheetManager, self).get_query_set().filter(working_date=date.today())

    def getTimeSheetForToday(self, user):
        entry = super(TimeSheetManager, self).get_query_set().filter(user=user,working_date=date.today())
        if not entry:
#             create entry for today
            timesheet = TimeSheet(user=user, working_date=date.today())
            timesheet.save()
            return timesheet
        else:
            return entry







class UserTimeSheet(models.Model):

    STATUS_CHOICES = (
    ('normal', 'normal'),
    ('good', 'good'),
    ('late', 'late'),
    )
    user = models.ForeignKey(User)
    working_date = models.DateField(null=True)
    check_in = models.TimeField(null=True,blank=True)
    check_out = models.TimeField(null=True,blank=True)
    level = models.SmallIntegerField(null=True,blank=True,default=0)
    fines = models.DecimalField(max_digits=12,decimal_places=2,blank=True,null=True,default=0)
    status = models.CharField(max_length=10,null=True,blank=True,choices=STATUS_CHOICES)
    special = models.BooleanField(default=False)
    payment = models.BooleanField(default=False)
    objects = TimeSheetManager()


    def get_all(self):
        return UserTimeSheet.objects.filter(working_date=date.today())


    def save(self):
        super(UserTimeSheet,self).save()

    def __unicode__(self):
        return str("%s %s" % (self.user.username, str(self.working_date)))

    class Meta:
        verbose_name_plural = 'Management Time User'




class TimeWorking(models.Model):
    STATUS_CHOICES = (
    ('morning', 'morning'),
    ('noon', 'noon'),
    ('full', 'full'),
    )
    user = models.ForeignKey(User)
    working_date = models.DateField(null=True,blank=True)
    state = models.CharField(max_length=50,null=True,blank=True,choices=STATUS_CHOICES)
    note = models.TextField(null=True,blank=True)
    def __unicode__(self):
         return "%s" % self.user

    def save(self):
        try:
            usertimesheet = UserTimeSheet.objects.get(user=self.user,working_date__day=self.working_date.day,
                                                  working_date__year=self.working_date.year,
                                                  working_date__month=self.working_date.month)
        except:
            usertimesheet = UserTimeSheet(user=self.user)
            usertimesheet.working_date = self.working_date

        usertimesheet.special = True
        usertimesheet.save()
        return super(TimeWorking,self).save()

    class Meta:
        verbose_name_plural = 'Working'


class Report(models.Model):
    user = models.ForeignKey(User)
    month = models.IntegerField(null=True,blank=True)
    year = models.IntegerField(null=True,blank=True)
    fines = models.DecimalField(max_digits=12,decimal_places=2,null=True,blank=True,default=0.0)
    leave_days = models.IntegerField(default=0)
    note = models.TextField(null=True,blank=True)

    def __unicode__(self):
         return '%s' % self.fines

    class Meta:
         verbose_name_plural = 'Report'


class TimeSheet(models.Model):
    morning_time_start = models.TimeField(null=True)
    morning_time_end = models.TimeField(null=True)
    afternoon_time_start = models.TimeField(null=True)
    afternoon_time_end = models.TimeField(null=True)
    note = models.TextField(null=True,blank=True)
    def __unicode__(self):
         return "start = %s , end = %s" % (self.morning_time_start,self.afternoon_time_end)

    class Meta:
         verbose_name_plural = 'Time Working'




class TimeSheetMoney(models.Model):
    fines_company_late = models.DecimalField(max_digits=12,decimal_places=2,null=True,blank=True,default=0.0)
    fines_home_early = models.DecimalField(max_digits=12,decimal_places=2,null=True,blank=True,default=0.0)
    method = models.CharField(max_length=1,null=True,blank=True,choices=(('*','*'),('+','+')))
    exp = models.DecimalField(max_digits=3,decimal_places=2,null=True,blank=True,default=0.0)
    note = models.TextField(null=True,blank=True)

    def __unicode__(self):
         return '%s' % self.fines_company_late
    class Meta:
         verbose_name_plural = 'Money'

# class Settings(models.Model):
#     receive_newsletter = models.BooleanField()
#
#
#
# def system_check():
#     for user in User.objects.all():
#         try:
#             people = UserTimeSheet.objects.get(user=user,working_date=date.today())
#         except:
#             people = UserTimeSheet(user=user,working_date=date.today())
#             people.save()


