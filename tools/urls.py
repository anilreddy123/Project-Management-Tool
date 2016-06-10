from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
    #url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', logout_page),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
    url(r'^register/$', register),

    url(r'^$', home, name="home"),
    url(r'^register/success/$', register_success),
    #url(r'^createteam/$', create_team),
    url(r'^addproject/$', addproject),
    url(r'^addtask/$', addtask),
    url(r'^delete_task/(\d+)/$', delete_task),
    url(r'^getproject/$', get_project),
    url(r'^gettask/(\d+)/$', get_task),

)
