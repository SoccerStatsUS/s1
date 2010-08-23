from django.core.cache import cache
from django.shortcuts import render_to_response
from django.template import RequestContext

from soccer.teams.models import Team

def index(request):
    teams = Team.objects.order_by("short_name")
    return render_to_response("teams/index.html",
                              {"teams": teams},
                              context_instance=RequestContext(request)
                              )

def team_by_slug(request, slug):
    return team_view(request, Team.objects.get(slug=slug))

def team_by_id(request, id):
    return team_view(request, Team.objects.get(id=id))

def team_view(request, team):
    return render_to_response("teams/team.html",
                              {"team": team},
                              context_instance=RequestContext(request)
                              )
    

