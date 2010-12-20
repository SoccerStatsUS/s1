import datetime

from django.core.cache import cache
from django.shortcuts import render_to_response
from django.template import RequestContext

from soccer.leagues.models import League
from soccer.players.models import Person
from soccer.salaries.models import Salary
from soccer.stats.models import SeasonStat
from soccer.teams.models import Team

from django import forms

def get_salary_year_form(year):
    
    league = League.objects.get(name="Major League Soccer")
    team_ids = set([e[0] for e in SeasonStat.objects.filter(year=year).values_list("team")])
    teams = Team.objects.filter(league=league, id__in=team_ids)

    team_choices = [(0, "All Teams")]
    team_choices.extend([(e.id, e) for e in teams])
    
    class SalaryYearForm(forms.Form):
        team = forms.ChoiceField(team_choices)

    return SalaryYearForm

    
def minutes_per_hundred_dollars(year):
    """Return the most overpaid and underpaid players by minutes played."""
    salaries = Salary.objects.filter(year=year)
    bases = salaries.values_list("player", "base")
    player_ids = [e[0] for e in bases]
    players = Person.objects.filter(id__in=player_ids)
    players_dict = dict([(e.id, e) for e in players])
    minutes_list = SeasonStat.objects.filter(year=year, player__in=player_ids).values_list("player", "minutes")
    minutes_dict = dict(minutes_list)

    d = {}
    for player_id, base in bases:
        minutes = minutes_dict.get(player_id, 0)
        minutes_per_dollar = minutes / float(base)
        player = players_dict[player_id]
        d[player] = (100*minutes_per_dollar, base, minutes, player_id)
    sorted_production = sorted(d.items(), key=lambda e: e[1])

    return sorted_production
        
        
        
def get_salary_years():
    CACHE_KEY = "salary_years"
    years = cache.get(CACHE_KEY)
    if years is None:
        years = sorted(set([e.year for e in Salary.objects.all()]))
        cache.set(CACHE_KEY, years)
    return years
        


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

    context = {
        "team_numbers": team_numbers,
        "salary_years": get_salary_years(),
        }

    return render_to_response('salaries/index.html', 
                              context,
                              context_instance=RequestContext(request)
                              )

def by_year(request, year):
    CACHE_KEY = "salaries:%s" % year
    salaries = cache.get(CACHE_KEY)
    if salaries is None:
        salaries = Salary.objects.filter(year=year).order_by('-base')
        cache.set(CACHE_KEY, salaries, 60*60*24*7)

    if (request.GET.get("team")):
        try:
            team_id = int(request.GET.get('team'))
            if team_id:
                team = Team.objects.get(id=team_id)
                salaries = salaries.filter(team2=team)
        except ValueError:
            pass
        
    form = get_salary_year_form(year)
    return render_to_response('salaries/list.html',
                              {"salaries": salaries,
                               "form": form(),
                               "year": year,
                               },
                              context_instance=RequestContext(request)
                              )

def by_year_highlights(request, year):
    CACHE_KEY = "salaries:highlights:%s" % year
    salaries = cache.get(CACHE_KEY)
    if salaries is None:
        salaries = Salary.objects.filter(year=year).order_by('-base')
        cache.set(CACHE_KEY, salaries, 60*60*24*7)


    
    count = salaries.count()
    highest = salaries[:10]
    lowest = salaries[count - 10:count]

    b = reversed(minutes_per_hundred_dollars(year)[-20:])
    best_deals = [(e[0], e[1][0], e[1][1], e[1][2], e[1][3]) for e in b]

    context = {
        "highest": highest,
        "lowest": lowest,
        "best_deals": best_deals,
        }


    return render_to_response('salaries/highlights.html',
                              context,
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
    
