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
    from timesheet.models import TimeSheet
    from datetime import datetime,date
    time = TimeSheet.objects.get(pk=1)
    now = datetime.now()

    print str(morning) == str(None)
    if (str(morning) == str(None) and time.afternoon_time_end.hour > now.time().hour > time.morning_time_start.hour - 2):
        return """$('#demo').text("");
             $('#demo').append("<div class='i_footer'><button name='checkin' type='submit' class='btn btn-default btn-lg btn-theme'>Check In</button></div>")
             """
    elif (not afternoon):
        return """$('#demo').text("");
             $('#demo').append("'<div class='i_footer'><button name='home' type='submit' class='btn btn-default btn-lg btn-theme'>Home</button><button name='checkout' type='submit' class='btn btn-default btn-lg btn-theme'>Check Out</button></div>")
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