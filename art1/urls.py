from art1.views import detail
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

                       url(r'^$', detail),
                       )