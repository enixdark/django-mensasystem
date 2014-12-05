from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    url(r'^admin/sendmessage/$','message.views.form_send_message'),
    url(r'^sendmessage/$','message.views.form_send_message'),
    url(r'^fullview/$','message.views.form_full_view'),

)
