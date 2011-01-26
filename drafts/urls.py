from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('soccer.drafts.views', 
                       url(r'^$',
                           'draft_index',
                           name='draft_index'),

                       url(r'^dashboard/$',
                           'usmnt_dashboard',
                           name='dashboard'),

                       url(r'^bigboard/$',
                           'big_board',
                           name='big_board'),


                       url(r'^(?P<id>\d+)/$',
                           'draft_detail',
                           name='draft_detail'),

                       url(r'^player/(?P<player_id>\d+)/$',
                           'usmnt_draft_player',
                           name='usmnt_draft_player'),


                       url(r'^usmnt/(?P<id_1>\d+)/(?P<id_2>\d+)/$',
                           'draft_compare',
                           name='draft_compare'),

                       url(r'^usmnt/overview/$',
                           'usmnt_draft_overview',
                           name='usmnt_draft_overview'),


)
