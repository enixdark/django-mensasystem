import cronjobs
from ..timesheet.models import UserTimeSheet,TimeWorking,TimeSheetMoney,Report,TimeSheet
from django.contrib.auth.models import User
from datetime import date,timedelta,datetime
from django.db import models
from decimal import Decimal
import math
@cronjobs.register
def cron_user():
    users = User.objects.all()
    today = date.today()
    time_working = TimeSheet.objects.all()[0]
    punish = TimeSheetMoney.objects.first()

    for people in users:
        try:
            people_have = UserTimeSheet.objects.get(user = people,working_date = today)
        except UserTimeSheet.DoesNotExist:
            people_have = UserTimeSheet(user = people,working_date = today)
            try:
                work_have = TimeWorking.objects.get(user = people,working_date = today)
                people_have.special = True
            except TimeWorking.DoesNotExist:
                try:
                    report = Report.objects.get(user = people,month=today.month)
                except Report.DoesNotExist:
                    report = Report(user = people,month=today.month , year = today.year)
                money = Decimal(punish.fines_not_checkin)
                now = datetime.now().time()
                people_have.check_in = now
                people_have.check_out = now
                people_have.fines = Decimal(people_have.fines) + money
                report.fines = Decimal(report.fines) + money
                report.save()
            people_have.save()


@cronjobs.register
def cron_user_notcheckout():

    users = User.objects.all()
    today = date.today()
    time_working = TimeSheet.objects.all()[0]
    punish = TimeSheetMoney.objects.first()
    for people in users:
        people_have = UserTimeSheet.objects.get(user = people,working_date = today)
        try:
            work_have = TimeWorking.objects.get(user = people,working_date = today)
        except:
            work_have.state = None
        print  people_have,work_have.state not in ['noon','full'] and people_have.check_out is None

        if (work_have.state not in ['noon','full']) and people_have.check_out is None:
            try:
                report = Report.objects.get(user = people,month=today.month)
            except Report.DoesNotExist:
                report = Report(user = people,month=today.month , year = today.year)
            money = Decimal(punish.fines_not_checkout)
            people_have.fines = Decimal(people_have.fines) + money
            report.fines = Decimal(report.fines) + money
            report.save()
        people_have.save()
