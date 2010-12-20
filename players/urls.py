from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('soccer.players.views', 
                       url(r'^$',
                           'person_index',
                           name='person_index'),

                       

                       url(r'^nobirthdate/$',
                           'no_birthdate',
                           name='no_birthdate'),

                       url(r'^nobirthplace/$',
                           'no_birthplace',
                           name='no_birthplace'),

                       url(r'^nofirstname/$',
                           'no_firstname',
                           name='no_firstname'),




                       url(r'^(?P<id>\d+)/$',
                           'person_detail_id',
                           name='person_detail_id'),

                       url(r'^n/(?P<slug>.*)/$',
                           'person_detail_slug',
                           name='person_detail_slug'),

                       url(r'^sn/(?P<id>.*)/$',
                           'soccernet_bio_detail',
                           name='soccernet_bio_detail'),




)
