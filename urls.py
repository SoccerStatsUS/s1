from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', include('soccer.main.urls')),
                       url(r'^salaries/', include('soccer.salaries.urls')),
                       url(r'^teams/', include('soccer.teams.urls')),
                       url(r'^leagues/', include('soccer.leagues.urls')),
                       url(r'^international/', include('soccer.international.urls')),                       
                       

                       # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
                       # to INSTALLED_APPS to enable admin documentation:
                           (r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       # Uncomment the next line to enable the admin:
                           (r'^admin/', include(admin.site.urls)),
)
