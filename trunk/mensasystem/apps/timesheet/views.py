#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, HttpResponseRedirect, HttpResponse,RequestContext
from django.views.generic import TemplateView
from django.shortcuts import render
from dateutil.parser import parse
from django.db.models import Q, Sum

# from timesheet.models import TimeSheet,UserTimeSheet
from .models import *

# Create your views here.

class TimeSheetView(TemplateView):
    template_name = 'timesheet/timesheet.html'
    context_object_name = 'context'
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super(TimeSheetView, self).get_context_data(**kwargs)
        context['timesheet_today'] = TimeSheet.objects.getTimeSheetForToday(self.request.user)
        context['timesheet_list'] = TimeSheet.objects.getTimeSheetForUser(self.request.user)
        return context

class TimeSheetReportView(TemplateView):
    template_name = 'timesheet/timesheetreport.html'
    
    def get_context_data(self, **kwargs):
        context = TemplateView.get_context_data(self, **kwargs)
        return context



def coming(request,next = '/dashboard/'):

    from .models import TimeSheet
    from datetime import datetime,date,timedelta
    from decimal import Decimal
    from .custom import method_payment
    if not request.user.is_active:
        return HttpResponseRedirect(next)


    today = date.today()
    try:
        time_working = TimeSheet.objects.get(user = request.user)
        punish = TimeSheetMoney.objects.all()[0]
    except:
        return HttpResponseRedirect('/error606/')

    try:
        work = TimeWorking.objects.get(user = request.user,working_date=today)
    except TimeWorking.DoesNotExist:
        work = None

    try:
        report = Report.objects.get(user = request.user,month=today.month)
    except Report.DoesNotExist:
        report = Report(user = request.user,month=today.month , year = today.year)

    try:
        if today.strftime("%A") in ['Monday']:
            day = today + timedelta(days=-3)
        else:
            day = today + timedelta(days=-1)
        pre = UserTimeSheet.objects.get(user = request.user,working_date=day)
    except UserTimeSheet.DoesNotExist:
        pre = UserTimeSheet()

    try:
        time = UserTimeSheet.objects.get(user = request.user,working_date__year=today.year,working_date__month=today.month,working_date__day=today.day)
    except UserTimeSheet.DoesNotExist:
        time = UserTimeSheet(user = request.user,fines= method_payment(punish.fines_company_late,punish.method,punish.exp,pre.level,punish.block,work,time_working,'late'))
        report.fines = Decimal(report.fines) +  Decimal(time.fines) if time.fines!=None else Decimal(0)

    if request.method == 'POST':
        if 'home' in request.POST:
            return HttpResponseRedirect(next)
        time.working_date =  date.today()
        pay = method_payment(punish.fines_company_late,punish.method,punish.exp,pre.level,punish.block,work,time_working,'late')
        if 'checkin' in request.POST:
            time.check_in = datetime.now()
            if work:
                if work.state == 'morning':
                    if time.check_in.time() > time_working.afternoon_time_start:
                        time.status = 'late'
                        time.level = pre.level + 1
                    else:
                        time.status = 'normal'
                        report.fines -= pay
                        time.fines -= pay
                        time.level = 0
                time.special = True
            else:
                if time.check_in.time() > time_working.morning_time_start:
                    time.status = 'late'
                    time.level = pre.level + 1
                else:
                    time.status = 'normal'
                    report.fines -= pay
                    time.fines -= pay
                    time.level = 0
        elif 'checkout' in request.POST:
            if not time.check_out:
                if (work and work.state in ['full','noon']) or datetime.now().time() > time_working.afternoon_time_end:
                    time.payment = True
                else:
                    pay =  method_payment(punish.fines_home_early,punish.method,punish.exp,pre.level,punish.block,work,time_working,'ealry')
                    time.fines += pay
                    report.fines += pay
                if time.status is None:
                    time.status = 'late'
                    time.level = pre.level + 1
                if time.status == 'normal':
                    time.status = 'good'
                    time.payment = True

            time.check_out = datetime.now()
        time.save()
        report.save()
        return HttpResponseRedirect('/dashboard/')

    return render_to_response('Coming.html',{'time':time_working,'user_time':time},
                              context_instance=RequestContext(request))




def get_fines_from_date(request,date):
    import json

    data = {'fines':0,'total_working':0,'total_not_working':0}
    month = parse(date).month
    year = parse(date).year
    try:
        data['fines']  = float(Report.objects.get(user=request.user,month=month , year = year).fines)
        db =  UserTimeSheet.objects.filter(user=request.user,working_date__month=month ,working_date__year = year)
        data['total_working']  = db.count()
        data['total_not_working']  = db.filter(special=True).count()
    except:
        pass

    return HttpResponse(json.dumps(data,separators=(',', ': ')))

def jsondump_week(request,year):
    import json
    from datetime import date, timedelta
    begin = date(int(year),1,1)
    end = begin - timedelta(begin.weekday())
    tup = []
    for i in range(1,53):
        dlt = timedelta(days = (i-1)*7)
        start_date = (end + dlt)
        end_date = (end + dlt + timedelta(days=4))
        tup.append({'week':i,'description':"%s -> %s" % (start_date.strftime('%m/%d') , end_date.strftime('%m/%d')),'time':'%s , %s' % (start_date,end_date)})
    return HttpResponse(json.dumps(tup,separators=(',', ': ')))

def report(request):
    from datetime import date
    month = date.today().month
    year = date.today().year
    data = Report.objects.all()
    result = data.filter(month = month,year = year)

    if not result:
        for user in User.objects.all():
            try:
                report = result.get(user = user , month = month , year = year)
            except:
                report = Report(user = user , month = month , year = year)
            report.save()
    sum = data.aggregate(Sum('fines'))

    return render_to_response('report.html',{'request':request,'user':request.user,'data':Report.objects.all().order_by('-month'),'sum':sum})


def report_week(request):
    from datetime import date
    query_user = Q()
    people = User.objects.all()
    end = date.today()
    start = date.today()
    if request.GET:
        year = request.GET['year']
        week = request.GET['week'].split(',')
        start = parse(week[0]).replace(int(year))
        end = parse(week[1]).replace(int(year))
        # Convert a Querydict from GET data to string and extract a collection of user
        if request.GET.get('user',False):
            s = str(request.GET)
            be = s.find(u'user')
            ed = s[be:].find(']')
            users = eval(s[be+6:be+ed+1])
            if users:
                query_user = Q(user__email = users.pop())
                for p in users:
                    query_user = query_user | Q(user__email= p )
    data = UserTimeSheet.objects.filter(query_user & Q(working_date__lt = end) & Q(working_date__gt = start))

    sum = data.aggregate(Sum('fines'))

    return render_to_response('report_result_from_week.html',{'request':request,'user':request.user,
                                                              'data':data,'sum':sum,
                                                              'people':people})

def error_page(request):
    return render_to_response('time_working.html', {'request': request, 'user': request.user})



