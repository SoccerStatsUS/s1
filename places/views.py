from django.core.cache import cache
from django.shortcuts import render_to_response
from django.template import RequestContext

from soccer.places.models import Country
from soccer.players.models import Person



def country_index(request):
    countries = Country.objects.all()
    return render_to_response("places/index.html",
                              {"countries": countries},
                              context_instance=RequestContext(request)
                              )    

def country_detail(request, id):
    country = Country.objects.get(id=id)
    people = Person.objects.filter(nationality=country)
    return render_to_response("places/country_detail.html",
                              {"people": people},
                              context_instance=RequestContext(request)
                              )    
    
