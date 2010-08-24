from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('soccer.players.views', 
                       url(r'^$',
                           'person_index',
                           name='person_index'),

                       url(r'^(?P<id>\d+)/$',
                           'person_detail',
                           name='person_detail'),

)
