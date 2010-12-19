from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('soccer.feeds.views', 
                       url(r'^$',
                           'story_list',
                           name='story_list'),
)
