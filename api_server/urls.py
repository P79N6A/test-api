from django.conf.urls import patterns, url, include

urlpatterns = patterns('',

    url(r'^health', 'api_server.views.health'),


)
