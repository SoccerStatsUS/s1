from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('soccer.lineups.views', 
                       url(r'^$',
                           'index',
                           name='schedule_index'),

                       url(r'^(?P<year>\d+)/$',
                           'year_schedule',
                           name='year_schedule'),

                       url(r'^game/(?P<game_id>\d+)/$',
                           'game_detail',
                           name='game_detail'),


)
