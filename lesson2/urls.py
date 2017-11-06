from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView



admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^blog/$', include('blog.urls')),
                       url(r'^$', include('art1.urls')),
                       url(r'^app2/', include('app2.urls')),
                       url(r'^fav/', include('favorite.urls')),
                       url(r'^home/', include('home.urls')),
                       url(r'^app3/$', include('app3_filters.urls')),

                       )

urlpatterns += patterns('mytest.views',
                        url(r'^test$', 'my_test_func'),
                       (r'^about/', TemplateView.as_view(template_name='about.html'))
                       )
