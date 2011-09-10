from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from soccer.lineups.models import Game

import datetime

def index(request):
    context = {"years": range(1996, 2011),
               }

    return render_to_response("schedule/index.html",
                              context,
                              context_instance=RequestContext(request))


def year_schedule(request, year):
    games = Game.objects.filter(date__year=year)
    context = {
        'games': games,
        }
    return render_to_response("schedule/schedule.html",
                              context,
                              context_instance=RequestContext(request))


def game_detail(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    context = {
        'game': game,
        'goals': game.goals.all(),
        }
    return render_to_response("schedule/game.html",
                              context,
                              context_instance=RequestContext(request))


def scores_index(request):
    games = Game.objects.filter(date=datetime.date.today()).order_by("-date")
    games = Game.objects.order_by("-date")[:50]
    context = {
        'games': games,
        }
    return render_to_response("schedule/scores.html",
                              context,
                              context_instance=RequestContext(request))



    
