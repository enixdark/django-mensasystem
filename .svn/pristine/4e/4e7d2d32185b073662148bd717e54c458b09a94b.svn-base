import cronjobs
from timesheet.models import UserTimeSheet,TimeWorking,TimeSheetMoney,Report
from django.contrib.auth.models import User
from datetime import date,timedelta
from django.db import models

@cronjobs.register
def cron_user():

    def method_payment(punish,method,exp,level):
        if method == '*':
            return punish*exp**level
        elif method == '+':
            return punish + exp

    users = User.objects.all().exclude(is_superuser=True)
    today = date.today()
    punish = TimeSheetMoney.objects.all()[0]

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
                    if today.strftime("%A") in ['Monday']:
                        day = today + timedelta(days=-3)
                    else:
                        day = today + timedelta(days=-1)
                    pre = UserTimeSheet.objects.get(user = people,working_date=day)
                except UserTimeSheet.DoesNotExist:
                    pre = UserTimeSheet()
                try:
                    report = Report.objects.get(user = people,month=today.month)
                except Report.DoesNotExist:
                    report = Report(user = people,month=today.month , year = today.year)
                people_have.fines += method_payment(punish.fines_company_late,punish.method,punish.exp,pre.level)
                report.fines += method_payment(punish.fines_company_late,punish.method,punish.exp,pre.level)

            report.save()
            people_have.save()


