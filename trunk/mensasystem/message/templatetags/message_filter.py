from django import template
from django.template.defaultfilters import stringfilter
from message.models import User
from datetime import datetime
from dateutil import parser
from time import mktime,time
register = template.Library()

#
#

cache_message = {}
cache_time = {}
@register.filter(name='get_message')
def get_message(user):
    global cache_message
    if not cache_message.has_key(user):
        cache_message[user] = User.objects.get(email=user).message_set.all().order_by('-time')[:10]
    return cache_message[user]

intervals = (
    ('week', 604800),
    ('day', 86400),
    ('hours', 3600),
    ('minutes', 60),
    ('seconds', 1),
    )

@register.filter(name='convert_time')
def convert_time(t,granularity=1):
    global cache_message
    result = []
    now = time()
    pre = mktime(parser.parse(t).timetuple())
    seconds = now - pre
    for name, count in intervals:
        value = seconds // count
        if value:
            seconds -= value * count
            if value == 1:
                name = name.rstrip('s')
            result.append("{} {}".format(value, name))
    return ', '.join(result[:granularity])

@register.filter(name='refresh')
def refresh(user):
    global cache_message
    del cache_message[user]


@register.filter(name='make_range')
def make_range(num):
    return range(1,int(num)+1)






