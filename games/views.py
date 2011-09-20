import datetime

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from soccer.games.models import Game


def scores_index(request):
    games = Game.objects.filter(date=datetime.date.today()).order_by("-date")
    games = Game.objects.order_by("-date")[:50]
    context = {
        'games': games,
        }
    return render_to_response("games/scores.html",
                              context,
                              context_instance=RequestContext(request))


def game_detail(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    context = {
        'game': game,
        #'goals': game.goals.all(),
        }
    return render_to_response("games/detail.html",
                              context,
                              context_instance=RequestContext(request))




