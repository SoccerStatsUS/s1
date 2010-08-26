from django.core.cache import cache
from django.shortcuts import render_to_response
from django.template import RequestContext

from soccer.places.models import Country
from soccer.players.models import Person


def country_index(request):
    """A list of all the countries in the world."""
    # Consider filtering out countries without a player or a team.

    countries = Country.objects.all()
    return render_to_response("places/index.html",
                              {"countries": countries},
                              context_instance=RequestContext(request)
                              )    

def country_detail(request, id):
    """A detail view of a country.
    Contains listings of players and teams from the country.
    """

    country = Country.objects.get(id=id)
    people = Person.objects.filter(nationality=country)
    return render_to_response("places/country_detail.html",
                              {"people": people},
                              context_instance=RequestContext(request)
                              )    

def birthplace_detail(request, name):
    """Shows all people whose birthplace contains the given string."""
    # This is a pretty rough method.  We need some methods that automatically
    # improve birthplace descriptions.
    people = Person.objects.filter(birthplace__icontains=name)
    return render_to_response("places/country_detail.html",
                              {"people": people},
                              context_instance=RequestContext(request)
                              )        
    
