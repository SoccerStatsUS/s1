from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('soccer.lineups.views', 
                       url(r'^$',
                           'index',
                           name='schedule_index'),


                       url(r'^(?P<id>\d+)/$',
                           'game_detail',
                           name='game_detail'),


)
