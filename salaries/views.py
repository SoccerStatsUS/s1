import datetime

from django.core.cache import cache
from django.shortcuts import render_to_response
from django.template import RequestContext

from soccer.salaries.models import Salary


def index(request):
    most_recent_year = Salary.objects.order_by("-year")[0].year
    salaries = Salary.objects.filter(year=most_recent_year) 
    by_team = {}
    team_and_base = salaries.values_list("team", "base")
    
    for team, base in team_and_base:
        if team in by_team:
            by_team[team] += base
        else:
            by_team[team] = base
    team_numbers = sorted(by_team.items(), key=lambda e: -e[1])
    return render_to_response('salaries/index.html', 
                              {"team_numbers": team_numbers},
                              context_instance=RequestContext(request)
                              )

def by_year(request, year):
    CACHE_KEY = "salaries:%s" % year
    salaries = cache.get(CACHE_KEY)
    if salaries is None:
        salaries = Salary.objects.filter(year=year).order_by('-base')
        cache.set(CACHE_KEY, salaries, 60*60*24*7)
    return render_to_response('salaries/list.html',
                              {"salaries": salaries},
                              context_instance=RequestContext(request)
                              )

def by_team(request, year, team):
    CACHE_KEY = "salaries:%s:%s" % (year, team)
    salaries = cache.get(CACHE_KEY)
    years = Salary.get_years_for_team(team)
    if salaries is None:
        salaries = Salary.objects.filter(year=year, team=team).order_by('-base')
        cache.set(CACHE_KEY, salaries, 60*60*24*7)

    context = {"salaries": salaries,
               "years": years,
               "team": team,
               }
    return render_to_response('salaries/list.html',
                              context,
                              context_instance=RequestContext(request)
                              )

def by_team_this_year(request, team):
    most_recent_year = Salary.objects.order_by("-year")[0].year
    return by_team(request, most_recent_year, team)
    