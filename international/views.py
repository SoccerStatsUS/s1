from django.core.cache import cache
from django.shortcuts import render_to_response
from django.template import RequestContext

from soccer.international.models import Confederation

def index(request):
    """
    Listing of confederations.
    """
    # Better idea to exclude based on name.
    confederations = Confederation.objects.order_by("short_name").exclude(id=7)
    ctx = {
        "confederations": confederations
        }
    return render_to_response("international/index.html",
                              ctx,
                              context_instance=RequestContext(request)
                              ) 

def confederation_by_slug(request, slug):
    # Confederations don't have slugs yet.
    pass

def confederation_by_id(request, id):
    return confederation_view(request, Confederation.objects.get(id=id))

def confederation_view(request, confederation):
    # Stop doing this!
    leagues = confederation.leagues.all()
    context = {
        "leagues": leagues, 
        "confederation": confederation
        }
    return render_to_response("international/confederation.html",
                              context,
                              context_instance=RequestContext(request)
                              )    
    
    
