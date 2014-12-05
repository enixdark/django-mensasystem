from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
# import django_cron
# django_cron.autodiscover()


urlpatterns = patterns('',
    # Examples:
    url(r'^',include('mensa_app.urls')),
    url(r'^',include('timesheet.urls')),
    url(r'^',include('message.urls')),
    # url(r'^admin/', include('admins.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

# if settings.DEBUG:
# urlpatterns += patterns('',
#                         url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
#                             'document_root': settings.MEDIA_ROOT,
#                             }),
#                         )