from django.conf.urls.defaults import patterns, url
from piston.resource import Resource
from soccer.api.handlers import PersonHandler

person_handler = Resource(PersonHandler)

urlpatterns = patterns('',
   url(r'^players/(?P<post_slug>[^/]+)/', person_handler),
   url(r'^players/', person_handler),
)
