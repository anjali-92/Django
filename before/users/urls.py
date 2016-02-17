from django.conf.urls import patterns, include, url
from .views import SignUp

#Create your views here.

urlpatterns = patterns('users.views',
	url(r'^home$','home',name="users_home"),
	url(r'^signup$',SignUp.as_view(),name="user_signup"),
	)
