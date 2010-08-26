import datetime

from django.core.cache import cache
from django.shortcuts import render_to_response
from django.template import RequestContext

from soccer.stats.models import SeasonStat, CareerStat


def stats_index(request):
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

def year_stats(request, year):
    stats = SeasonStat.objects.filter(year=year).order_by("team")
    return render_to_response('stats/year.html',
                              {'stats': stats},
                              context_instance=RequestContext(request)
                              )
    
    
