from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('soccer.teams.views', 
                       url(r'^$', 'index', name='teams_index'),
                       url(r'^defunct/$', 'defunct', name='defunct_index'),

                       url(r'^(?P<slug>[a-zA-Z0-9_.-]+)/$',
                           'team_detail',
                           name='team_detail'),

                       url(r'^(?P<slug>[a-zA-Z0-9_.-]+)/schedule/(?P<year>\d+)/$',
                           'team_schedule_year',
                           name='team_schedule_year'),

                       url(r'^(?P<slug>[a-zA-Z0-9_.-]+?)/schedule/$',
                           'team_schedule',
                           name='team_schedule'),

                       url(r'^(?P<id>\d+)/(?P<year>\d+)/$',
                           'team_and_year',
                           name='team_and_year'),



)
