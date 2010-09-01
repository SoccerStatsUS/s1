from django.core.cache import cache
from django.shortcuts import render_to_response
from django.template import RequestContext

from soccer.teams.models import Team
from soccer.stats.models import SeasonStat

def index(request):
    """A list of all teams in the database."""

    teams = Team.objects.order_by("short_name")
    return render_to_response("teams/index.html",
                              {"teams": teams},
                              context_instance=RequestContext(request)
                              )

def team_and_year(request, id, year):
    """Detailed information for a team for a given year.
    Contains player stats and game details."""
    # Game details not yet implemented.

    team = Team.objects.get(id=id)
    stats = SeasonStat.objects.filter(team=team, year=year)
    context = {
        'team': team,
        'stats': stats,
        }
    return render_to_response("teams/team_and_year.html",
                              context,
                              context_instance=RequestContext(request)
                              )
                              

# Probably shouldn't be using both of these.  
# Should probably just be using slugs.

def team_by_slug(request, slug):
    return team_view(request, Team.objects.get(slug=slug))

def team_by_id(request, id):
    return team_view(request, Team.objects.get(id=id))

def team_view(request, team):
    years = team.years_with_stats()
    context = {
        'team': team,
        'years': years,
        }
    return render_to_response("teams/team.html",
                              context,
                              context_instance=RequestContext(request)
                              )
    

