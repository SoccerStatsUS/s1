import datetime

from django.core.cache import cache
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.cache import cache_page

from soccer.drafts.models import Draft, Pick
from soccer.players.models import Person


def draft_index(request):
    drafts = Draft.objects.all()
    return render_to_response("drafts/index.html",
                              {"drafts": drafts},
                              context_instance=RequestContext(request)
                              )    

def draft_detail(request, id):
    this_draft = Draft.objects.get(id=id)
    picks = Pick.objects.filter(draft=this_draft)

    other_drafts = Draft.objects.exclude(id=this_draft.id).values("id", "name")

    context = {
        "this_draft": this_draft,
        "picks": picks,
        "other_drafts": other_drafts,
        "teams": this_draft.teams(),
        "by_team": this_draft.by_team(),
        }

    
    return render_to_response("drafts/detail.html",
                              context,
                              context_instance=RequestContext(request)

                              )    

def usmnt_draft_player(request, player_id):
    p = Person.objects.get(id=player_id)
    l = []
    for pick in p.pick_set.filter(draft__name__contains="USMNT").order_by("draft__year"):
        l.append((p, pick.number, pick.draft.year))

    context = {
        'picks': l,
        }

    return render_to_response('drafts/usmnt_player.html',
                              context,
                              context_instance=RequestContext(request)
                              )

        
@cache_page(60 * 30)        
def usmnt_dashboard(request):
    """A dashboard of the current year's USMNT draft."""
    this_year = datetime.date.today().year
    usmnt_drafts = Draft.objects.filter(name__contains="USMNT Draft")
    current_draft = usmnt_drafts.get(year=this_year)
    previous_draft = usmnt_drafts.get(year=this_year - 1)
    return draft_compare(request, current_draft.id, previous_draft.id)


def draft_compare(request, id_1, id_2):

    CACHE_KEY = "draft_compare:%s:%s" % (id_1, id_2)

    context = cache.get(CACHE_KEY)

    if context is None:

        current_draft = Draft.objects.get(id=id_1)
        other_draft = Draft.objects.get(id=id_2)

        undrafted = other_draft.get_missing(current_draft)
        movement = current_draft.get_diff(other_draft)

        context = {
            'undrafted': undrafted,
            'movement': movement,
            'current_draft': current_draft,
            'other_draft': other_draft,
            'by_team': current_draft.by_team(),
            }

        if "USMNT" in current_draft.name and current_draft.year < 2010:
            scores = current_draft.score_draft(other_draft)
            context['scores'] = scores

        cache.set(CACHE_KEY, context, 3*60*60)

    return render_to_response('drafts/compare.html',
                              context,
                              context_instance=RequestContext(request)
                              )


def usmnt_draft_overview(request):

    drafts = Draft.objects.filter(name__contains="USMNT")

    average_ages = []
    for draft in drafts:
        a1 = draft.average_age(0, 50)
        a2 = draft.average_age(51, 100)
        a3 = draft.average_age(101, 150)
        total = draft.average_age()
        average_ages.append((draft.year, a1, a2, a3, total))
        
    context = {
        "average_age": average_ages,
        }

    return render_to_response('drafts/overview.html',
                              context,
                              context_instance=RequestContext(request)
                              )

    
@cache_page(60 * 30)
def big_board(request):
    """A board containing all USMNT draft picks of all time."""

    CACHE_KEY = "draft:big_board"

    context = cache.get(CACHE_KEY)


    if context is None:

        drafts = Draft.objects.filter(name__contains="USMNT")

        pick_sets = [e.pick_set.all().values_list("player__name", "player__id") for e in drafts]
        max_length = max([len(e) for e in pick_sets])

        backfill = lambda l, n: list(l) + [''] * (n - len(l))
        
        pick_map = zip(*[backfill(e, max_length) for e in pick_sets])

        context = {
            'pick_map': pick_map,
            'years': [e.year for e in drafts],
            }

        cache.set(CACHE_KEY, context, 60*60)

    return render_to_response('drafts/big_board.html',
                              context,
                              context_instance=RequestContext(request))

    
    
