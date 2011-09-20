from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('soccer.games.views', 
                       url(r'^$',
                           'scores_index',
                           name='scores_index'),

                       url(r'^game/(?P<game_id>\d+)/$',
                           'game_detail',
                           name='game_detail'),

)
