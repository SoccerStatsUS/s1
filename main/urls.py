from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('soccer.main.views', 
                       url(r'^$',
                           'index',
                           name='homepage'),


)
