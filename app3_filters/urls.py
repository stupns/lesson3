from django.conf.urls import patterns, include, url

urlpatterns = patterns('app3_filters.views',

                       url(r'$', 'filt'),
                           )
