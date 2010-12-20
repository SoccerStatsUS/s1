from django.core.cache import cache
from django.shortcuts import render_to_response
from django.template import RequestContext

from soccer.feeds.models import Feed, Entry

def index(request):
    news = Entry.objects.order_by("-pub_date")[:5]

    return render_to_response("index.html",
                              {"news": news},
                              context_instance=RequestContext(request)
                              ) 

def about(request):
    return render_to_response("about.html",
                              {},
                              context_instance=RequestContext(request)
                              ) 
