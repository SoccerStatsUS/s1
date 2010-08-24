from django.core.cache import cache
from django.shortcuts import render_to_response
from django.template import RequestContext

from soccer.drafts.models import Person



def person_index(request):
    people = Person.objects.all()
    no_person = Person.objects.get(name='No Person')
    context =  {
        "people": people,
        "no_person": no_person,
        }
    return render_to_response("players/index.html",
                              context,
                              context_instance=RequestContext(request)
                              )    

def person_detail(request, id):
    person = Person.objects.get(id=id)
    return render_to_response("players/detail.html",
                              {"person": person},
                              context_instance=RequestContext(request)
                              )    
    
