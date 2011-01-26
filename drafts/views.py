import datetime

from django.core.cache import cache
from django.shortcuts import render_to_response
from django.template import RequestContext

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

        
        

def usmnt_dashboard(request):
    this_year = datetime.date.today().year
    usmnt_drafts = Draft.objects.filter(name__contains="USMNT Draft")
    current_draft = usmnt_drafts.get(year=this_year)
    previous_draft = usmnt_drafts.get(year=this_year - 1)
    return draft_compare(request, current_draft.id, previous_draft.id)


def draft_compare(request, id_1, id_2):

    current_draft = Draft.objects.get(id=id_1)
    other_draft = Draft.objects.get(id=id_2)

    undrafted = other_draft.get_missing(current_draft)
    new = current_draft.get_missing(other_draft)
    movement = current_draft.get_diff(other_draft)

    context = {
        'new': new,
        'undrafted': undrafted,
        'movement': movement,
        }

    return render_to_response('drafts/compare.html',
                              context,
                              context_instance=RequestContext(request)
                              )
    
    
    
def usmnt_draft_compare(request, id_1, id_2):
    d1 = Draft.objects.get(id=id_1)
    d2 = Draft.objects.get(id=id_2)

    

    d1_results = dict([(e.player, e.number) for e in d1.pick_set.all()])
    d2_results = dict([(e.player, e.number) for e in d2.pick_set.all()])

    on = {}
    diff = {}
    off = {}

    for k, v in d1_results.items():
        if k not in d2_results:
            off[k] = v
        else:
            v2 = d2_results[k]
            diff[k] = (v, v2, v-v2)

    for k, v in d2_results.items():
        if k not in d1_results:
            on[k] = v

    prepare = lambda d: sorted(d.items(), key=lambda e: e[1])
    
    context = {
        "on": prepare(on),
        "off": prepare(off),
        "diff": sorted(diff.items(), key=lambda e: e[1][0]),
        }
    
    return render_to_response("drafts/compare.html",
                              context,
                              context_instance=RequestContext(request))
            
    
    
    
