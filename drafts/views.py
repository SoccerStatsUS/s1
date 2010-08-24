from django.core.cache import cache
from django.shortcuts import render_to_response
from django.template import RequestContext

from soccer.drafts.models import Draft, Pick



def draft_index(request):
    drafts = Draft.objects.all()
    return render_to_response("drafts/index.html",
                              {"drafts": drafts},
                              context_instance=RequestContext(request)
                              )    

def draft_detail(request, id):
    draft = Draft.objects.get(id=id)
    picks = Pick.objects.filter(draft=draft)
    return render_to_response("drafts/detail.html",
                              {"picks": picks},
                              context_instance=RequestContext(request)
                              )    
    
