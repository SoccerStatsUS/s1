from django.core.cache import cache
from django.core.paginator import Paginator, InvalidPage
from django.shortcuts import render_to_response
from django.template import RequestContext

from soccer.drafts.models import Person
from soccer.stats.models import SeasonStat, CareerStat


def person_index(request):
    no_person = Person.objects.get(name='No Person')



    letter = request.GET.get('l', 'a')
    qs = Person.objects.filter(last_name__istartswith=letter)

    paginator = Paginator(qs, 50)

    try:
        page_number = int(request.GET.get('page', '1'))
    except:
        page_number = 1

    try:
        person_page = paginator.page(page_number)
    except InvalidPage:
        raise Http404
    
    
    context =  {
        "people": person_page,
        "no_person": no_person,
        "letters": "abcdefghijklmonpqrstuvwxyz",
        }
    return render_to_response("players/index.html",
                              context,
                              context_instance=RequestContext(request)
                              )    

def person_detail(request, id):
    person = Person.objects.get(id=id)
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
    
