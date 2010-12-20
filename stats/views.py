import datetime

from django.core.cache import cache
from django.shortcuts import render_to_response
from django.template import RequestContext

from soccer.stats.models import SeasonStat, CareerStat


mosts = [
    "games_played", 
    "games_started", 
    "minutes", 
    "goals", 
    "assists", 
    "shots", 
    "fouls_committed", 
    "fouls_suffered", 
    "offsides"
    ]


most_tuples = [(e.replace("_", " ").title(), e) for e in mosts]


def stats_index(request):
    years = sorted(set([e[0] for e in SeasonStat.objects.all().values_list("year")]))

    context = {
        "mosts": most_tuples,
        "years": years,
        }

    return render_to_response('stats/index.html', 
                              context,
                              context_instance=RequestContext(request)
                              )

def year_leaders(request, year):
    stats = SeasonStat.objects.filter(year=year)
    
    goals = list(stats.order_by("-goals")[:10])
    assists = list(stats.order_by("-assists")[:10])
    offsides = list(stats.order_by("-offsides")[:10])

    table_attrs = [("GP", "games_played"), 
                   ("GS", "games_started"),
                   ("Goals", "goals"),
                   ("Assists", "assists"),
                   ("Offsides", "offsides"),
                   ]


    context = {
        "goals": goals,
        "assists": assists,
        "offsides": offsides,
        "table_attrs": table_attrs,
        }

    return render_to_response('stats/year_leaders.html', 
                              context,
                              context_instance=RequestContext(request)
                              )


def career_leaders(request, field):
    field = field.replace("-", "_")
    most = CareerStat.objects.order_by("-%s" % field)[:50]

    context = {
        "most": most,
        "table_attrs": most_tuples,
        }
    return render_to_response('stats/most.html', 
                              context,
                              context_instance=RequestContext(request)
                              )    
    

def year_stats(request, year):
    stats = SeasonStat.objects.filter(year=year).order_by("team")
    return render_to_response('stats/year.html',
                              {'stats': stats},
                              context_instance=RequestContext(request)
                              )
    
    
