from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('soccer.leagues.views', 
                       url(r'^$',
                           'index',
                           name='leagues_index'),

                       url(r'^competitions/$',
                           'competition_index',
                           name='competition_index'),

                       url(r'^competitions/(?P<competition_id>\d+)/$',
                           'competition_detail',
                           name='competition_detail'),


                       url(r'^(?P<id>\d+)/$',
                           'league_by_id',
                           name='league_by_id'),
)
