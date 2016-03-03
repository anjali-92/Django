from django.conf.urls import url
from .views import ToDoTaskList
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
	    url(r'^todolist/$',ToDoTaskList.as_view()),
	]

urlpatterns = format_suffix_patterns(urlpatterns)

