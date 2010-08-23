from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('soccer.leagues.views', 
                       url(r'^$',
                           'index',
                           name='leagues_index'),

                       url(r'^(?P<id>\d+)/$',
                           'league_by_id',
                           name='league_by_id'),
)
