from django.core.cache import cache
from django.db.models import Q
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from soccer.games.models import Game
from soccer.teams.models import Team
from soccer.stats.models import SeasonStat


def index(request):
    """A list of all teams in the database."""

    teams = Team.reals.order_by("short_name")
    ctx = {"teams": teams}
    return render_to_response("teams/index.html",
                              ctx,
                              context_instance=RequestContext(request)
                              )

def defunct(request):
    """A list of all teams in the database."""

    teams = Team.defuncts.order_by("short_name")
    ctx = {"teams": teams}
    return render_to_response("teams/index.html",
                              ctx,
                              context_instance=RequestContext(request)
                              )

def team_schedule(request, slug):
    """
    Recent games played by this team.
    """
    games = Game.objects.filter(Q(home_team__slug=slug) | Q(away_team__slug=slug)
                                ).order_by("-date")

    context = {
        'games': games,
        }
    
    return render_to_response('teams/schedule.html',
                              context,
                              context_instance=RequestContext(request))

def team_schedule_year(request, slug, year):
    """
    Recent games played by this team.
    """
    games = Game.objects.filter(Q(home_team__slug=slug) | Q(away_team__slug=slug),
                                date__year=year).order_by("-date")
    context = {
        'games': games,
        }
    
    return render_to_response('teams/schedule.html',
                              context,
                              context_instance=RequestContext(request))


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
                              


def team_detail(request, slug):
    team = get_object_or_404(Team, slug=slug)
    years = team.years_with_stats()

    # Whoa whoa whoa what is this stuff?
    minutes = {}
    games = {}
    goals = {}
    assists = {}


    stats = SeasonStat.objects.filter(team=team)
    for stat in stats:
        player = stat.player
        if player not in minutes:
            minutes[player] = games[player] = goals[player] = assists[player] = 0
        minutes[player] += stat.minutes
        games[player] += stat.games_played
        goals[player] += stat.goals
        assists[player] += stat.assists

    sort_leaders = lambda d: sorted(d.items(), key=lambda e: -e[1])

    context = {
        'team': team,
        'years': years,
        "minutes": sort_leaders(minutes)[:10],
        "games": sort_leaders(games)[:10],
        "goals": sort_leaders(goals)[:10],
        "assists": sort_leaders(assists)[:10],
        }

    return render_to_response("teams/team.html",
                              context,
                              context_instance=RequestContext(request)
                              )
    

