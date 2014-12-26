from django.conf.urls import patterns, url
from .views import TimeSheetView, TimeSheetReportView
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', TimeSheetView.as_view(), name='timesheet'),
    url(r'^admin/timesheet/report/$', 'apps.timesheet.views.report', name='report'),
    url(r'^admin/timesheet/report/week/$', 'apps.timesheet.views.report_week', name='report_week'),

    url(r'^jsondump/(?P<year>\d+)/$', 'apps.timesheet.views.jsondump_week', name='jsondump_week'),

    url(r'^fines/(?P<date>[\w\W\s]+)/$', 'apps.timesheet.views.get_fines_from_date', name='get_fines_from_date'),
    url(r'^error606/$','apps.timesheet.views.error_page'),
)