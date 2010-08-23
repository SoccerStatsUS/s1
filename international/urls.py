from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('soccer.international.views', 
                       url(r'^$',
                           'index',
                           name='international_index'),

                       url(r'^(?P<id>\d+)/$',
                           'confederation_by_id',
                           name='confederation_by_id'),

                       url(r'^(?P<slug>\w+)/$',
                           'confederation_by_slug',
                           name='confederation_by_slug'),

)
