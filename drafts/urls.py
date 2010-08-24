from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('soccer.drafts.views', 
                       url(r'^$',
                           'draft_index',
                           name='draft_index'),

                       url(r'^(?P<id>\d+)/$',
                           'draft_detail',
                           name='draft_detail'),

)
