from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('soccer.places.views', 
                       url(r'^$',
                           'country_index',
                           name='country_index'),

                       url(r'^(?P<id>\d+)/$',
                           'country_detail',
                           name='country_detail'),

)
