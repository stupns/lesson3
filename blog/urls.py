from django.conf.urls import patterns, include, url
from blog.views import mypost

urlpatterns = patterns('',
                       url(r'^$', mypost)
                       )
