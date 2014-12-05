from django.template import Library
from django.core.serializers import serialize
from django.db.models.query import QuerySet
from django.utils.safestring import mark_safe
from django import template
register = Library()

@register.filter
def get_fines( user , date ):
    from timesheet.models import Report
    from dateutil.parser import parse
    month = parse(date).month
    year = parse(date).year
    money = 0
    try:
        report = Report.objects.get(pk=user,month=month)
        money = report.fines
    except:
        pass
    return money

