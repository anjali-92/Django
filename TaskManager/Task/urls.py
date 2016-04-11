from django.conf.urls import url
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
	    url(r'^todolist/$',ToDoTaskList.as_view()),

	    url(r'^tasklist/(?P<status>[I|C]{1})/$',TaskList.as_view()),
	    url(r'^taskdetail/(?P<pk>[0-9]+)/$',TaskDetail.as_view()),
	    url(r'^users/$', UserList.as_view()),
	    url(r'^users/(?P<pk>[0-9]+)/$', UserDetail.as_view()),
	]

urlpatterns = format_suffix_patterns(urlpatterns)

