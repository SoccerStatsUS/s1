from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('soccer.scores.views', 
                       url(r'^$',
                           'scores_index',
                           name='scores_index'),
)
