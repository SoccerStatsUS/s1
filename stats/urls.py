from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('soccer.stats.views', 
                       url(r'^$',
                           'stats_index',
                           name='stats_index'),

                       url(r'^year/(?P<year>\d+)/$',
                           'year_leaders',
                           name='year_leaders'),

                       url(r'^most/(?P<field>\w+)/$',
                           'career_leaders',
                           name='career_leaders'),

                       url(r'^(?P<year>\d+)/$',
                           'year_stats',
                           name='year_stats'),

)
