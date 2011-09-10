from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('soccer.lineups.views', 
                       url(r'^$',
                           'scores_index',
                           name='scores_index'),

)
