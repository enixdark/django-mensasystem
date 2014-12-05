from django.conf.urls import patterns, url

from timesheet.views import TimeSheetView, TimeSheetReportView



urlpatterns = patterns('',
    url(r'^admin/timesheet/report/$', 'timesheet.views.report', name='report'),
    url(r'^fines/(?P<date>[\w\W\s]+)/$', 'timesheet.views.get_fines_from_date', name='get_fines_from_date'),
    url(r'^error606/$','timesheet.views.error_page'),

)