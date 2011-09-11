from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('soccer.teams.views', 
                       url(r'^$', 'index', name='teams_index'),
                       url(r'^defunct/$', 'defunct', name='defunct_index'),

                       url(r'^schedule/(?P<id>\d+)/(?P<year>\d+)/$',
                           'schedule',
                           name='schedule'),

                       
                       # Fixme
                       # This is obviously wrong.
                       # We want a slug match here.
                       url(r'^(?P<slug>.+)/$',
                           'team_detail',
                           name='team_detail'),

                       url(r'^(?P<id>\d+)/(?P<year>\d+)/$',
                           'team_and_year',
                           name='team_and_year'),

)
