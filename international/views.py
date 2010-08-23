from django.core.cache import cache
from django.shortcuts import render_to_response
from django.template import RequestContext

from soccer.international.models import Confederation

def index(request):
    confederations = Confederation.objects.order_by("short_name")
    return render_to_response("international/index.html",
                              {"confederations": confederations},
                              context_instance=RequestContext(request)
                              ) 

def confederation_by_slug(request, slug):
    pass

def confederation_by_id(request, id):
    return confederation_view(request, Confederation.objects.get(id=id))

def confederation_view(request, confederation):
    leagues = confederation.leagues.all()
    context = {"leagues": leagues, "confederation": confederation}
    return render_to_response("international/confederation.html",
                              context,
                              context_instance=RequestContext(request)
                              )    
    
    
