# from django.template import Library
# from django.core.serializers import serialize
# from django.db.models.query import QuerySet
# from django.utils.safestring import mark_safe
# from django import templates
# register = Library()

from django import template
from django.template.defaultfilters import stringfilter
# from django.templates.loader import render_to_string, TemplateDoesNotExist
register = template.Library()


@register.filter(name='get_text')
@stringfilter
def get_text(morning,afternoon):
    from ..models import TimeSheet
    from datetime import datetime,date
    time = TimeSheet.objects.get(pk=1)
    now = datetime.now()
    if (str(morning) == str(None) and time.afternoon_time_end.hour > now.time().hour >= time.morning_time_start.hour - 2):
        return """$('#demo').text("");
             $('#demo').append("<div class='i_footer'><button name='checkin' type='submit' class='btn btn-default btn-lg btn-theme'>Check In</button></div>")
             """
    elif (not afternoon):
        return """$('#demo').text("");
             $('#demo').append("'<div class='i_footer'><button  name='checkout' type='button' class='checkout btn btn-default btn-lg btn-theme' data-toggle='modal' data-target='#myModal'>Check Out</button></div>")
             """

    else:
        return """$('#demo').text("");
             $('#demo').append("<div class='i_footer'><button name='home' type='submit' class='btn btn-default btn-lg btn-theme'>Home</button></div>")
             """

@register.filter(name='filter_url')
def filter_url(url):
    urls = url.split('/')
    urllist = filter(lambda x: x!='',urls)
    data = []
    begin = url.find('/')
    while url.find('/',begin+1)!=-1:
        begin = url.find('/',begin+1)
        data.append(url[0:begin])
    return zip(urllist,data)


@register.filter(name='get_time')
def get_time(url):
    from datetime import datetime
    time = datetime.now().time()
    if url == 'hour':
        return time.hour
    elif url == 'minutes':
        return time.minute
    else:
        return time.second

@register.filter(name='is_checkin')
def is_checkin(id):
    from ..models import UserTimeSheet
    from datetime import date
    now = date.today()

    try:
        check = UserTimeSheet.objects.get(user_id = id,working_date=now)
    except:
        return True
    if check.check_in:
        return False
    return True


@register.filter(name='is_checkout')
def is_checkout(id):
    from ..models import UserTimeSheet
    from datetime import date
    now = date.today()
    try:
        check = UserTimeSheet.objects.get(user_id = id,working_date=now)
    except:
        return True
    if check.check_out:
        return False
    return True

@register.filter(name='get_week')
# def get_week(year, week):
def get_week(year):
    from datetime import date, timedelta
    begin = date(int(year),1,1)
    end = begin - timedelta(begin.weekday())
    tup = []
    for i in range(1,53):
        dlt = timedelta(days = (i-1)*7)
        start_date = (end + dlt)
        end_date = (end + dlt + timedelta(days=4))
        tup.append({'week':i,'description':"%s -> %s" % (start_date.strftime('%m/%d') , end_date.strftime('%m/%d')),'time':'%s , %s' % (start_date,end_date)})
    return tup


@register.filter(name='get_number_week')
def get_number_week(year):
    return range(1,54)

@register.filter(name='get_year')
def get_year(url):
    from datetime import datetime
    return range(2010,datetime.now().year + 1)