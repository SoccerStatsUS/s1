from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('soccer.stats.views', 
                       url(r'^$',
                           'stats_index',
                           name='stats_index'),

                       url(r'^(?P<year>\d+)/$',
                           'year_stats',
                           name='year_stats'),

)
