from django.core.cache import cache
from django.shortcuts import render_to_response
from django.template import RequestContext

from soccer.leagues.models import League
from soccer.teams.models import Team

def index(request):
    leagues = League.objects.order_by("name")
    return render_to_response("leagues/index.html",
                              {"leagues": leagues},
                              context_instance=RequestContext(request)
                              )

def league_by_id(request, id):
    league = League.objects.get(id=id)
    teams = Team.objects.filter(league=league)
    context = {"league": league,
               "teams": teams,
               }
    return render_to_response("leagues/league.html",
                              context,
                              context_instance=RequestContext(request)
                              )
    

