from django.conf.urls import patterns, include, url


urlpatterns = patterns('favorite.views',


                       url(r'$', 'fav'),
                           )