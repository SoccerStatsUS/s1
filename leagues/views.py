from django.core.cache import cache
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from soccer.leagues.models import League, Competition
from soccer.teams.models import Team

def index(request):
    leagues = League.objects.order_by("name")
    return render_to_response("leagues/index.html",
                              {"leagues": leagues},
                              context_instance=RequestContext(request)
                              )

def competition_index(request):
    competitions = Competition.objects.all()
    ctx = {
        'competitions': competitions,
        }
    return render_to_response("leagues/competitions.html",
                              ctx,
                              context_instance=RequestContext(request)
                              )

def competition_detail(request, competition_id):
    competition = get_object_or_404(Competition, id=competition_id)
    ctx = {
        'competition': competition,
        }
    return render_to_response("leagues/competition_detail.html",
                              ctx,
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
    

