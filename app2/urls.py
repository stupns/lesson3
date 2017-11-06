from django.conf.urls import patterns, include, url


urlpatterns = patterns('app2.views',

                       url(r'(?P<app2id>\d+)/$', 'detail' ),
                       url(r'list/$', 'reliz_list' ),
                       url(r'latest/$', 'latest1'),
                           )


