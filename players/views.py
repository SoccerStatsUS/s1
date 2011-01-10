from django.core.cache import cache
from django.shortcuts import render_to_response
from django.template import RequestContext

from soccer.players.models import Person, GenericBio
from soccer.stats.models import SeasonStat, CareerStat

def person_list_generic(request, person_list):
    context =  {
        "people": person_list,
        #"no_person": no_person,
        }
    return render_to_response("players/index.html",
                              context,
                              context_instance=RequestContext(request)
                              )    

def person_index(request):
    people = Person.objects.all()
    return person_list_generic(request, people)

def no_birthdate(request):
    people = Person.objects.filter(birthdate=None)
    return person_list_generic(request, people)

def no_birthplace(request):
    people = Person.objects.filter(birthplace='')
    return person_list_generic(request, people)

def no_firstname(request):
    people = Person.objects.filter(first_name='')
    return person_list_generic(request, people)


def person_detail(request, person):
    seasons = SeasonStat.objects.filter(player=person)
    career = CareerStat.objects.get(player=person)
    context = {
        "person": person,
        "seasons": seasons,
        "career": career,
        }
    return render_to_response("players/detail.html",
                              context,
                              context_instance=RequestContext(request)
                              )   

def soccernet_bio_detail(request, id):
    person = GenericBio.objects.get(id=id)
    context = {
        'person': person,
        }
    return render_to_response("players/sn_detail.html",
                              context,
                              context_instance=RequestContext(request)
                              )    

def person_detail_id(request, id):
    person = Person.objects.get(id=id)
    return person_detail(request, person)

def person_detail_slug(request, slug):
    person = Person.objects.get(mls_slug=slug)
    return person_detail(request, person)
    

    
