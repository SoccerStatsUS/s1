from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from soccer.lineups.models import Game

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


def game_detail(request, id):
    game = get_object_or_404(Game, id=id)
    context = {
        'game': game,
        }
    return render_to_response("schedule/game.html",
                              context,
                              context_instance=RequestContext(request))




    
