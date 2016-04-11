from django.conf.urls import patterns, include, url
from rest_framework import urls
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^task/',include('Task.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
