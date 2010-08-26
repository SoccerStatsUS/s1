from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('soccer.teams.views', 
                       url(r'^$',
                           'index',
                           name='teams_index'),

                       url(r'^(?P<id>\d+)/$',
                           'team_by_id',
                           name='team_by_id'),

                       url(r'^(?P<slug>\w+)/$',
                           'team_by_slug',
                           name='team_by_slug'),

                       url(r'^(?P<id>\d+)/(?P<year>\d+)/$',
                           'team_and_year',
                           name='team_and_year'),

)
