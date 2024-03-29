from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('soccer.salaries.views', 
                       url(r'^$',
                           'index',
                           name='salaries_index'),

                       url(r'^(?P<year>\d{4})/$',
                           'by_year',
                           name='salaries_by_year'),

                       url(r'^(?P<year>\d{4})/highlights$',
                           'by_year_highlights',
                           name='salaries_by_year_highlights'),

                       url(r'^(?P<team>\w+)/$',
                           'by_team_this_year',
                           name='salaries_by_team_this_year'),

                       url(r'^(?P<year>\d{4})/(?P<team>\w+)/$',
                           'by_team',
                           name='salaries_by_team')

)
