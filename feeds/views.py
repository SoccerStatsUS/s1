from django.core.paginator import Paginator, EmptyPage, InvalidPage

from django.shortcuts import render_to_response
from django.template import RequestContext

from soccer.feeds.models import Feed, Entry

ENTRIES_PER_PAGE = 25

def story_list(request):
    entries = Entry.objects.order_by("-pub_date")
    paginator = Paginator(entries, ENTRIES_PER_PAGE)

    if "source" in request.GET:
        entries = entries.filter(author=request.GET.get('source__name'))

    paginator = Paginator(entries, 20)
    
    try:
        page = int(request.GET.get("page", 1))
    except:
        page = 1

    try:
        paginator_page = paginator.page(page)
    except (EmptyPage, InvalidPage):
        paginator_page = paginator.page(1)

    return render_to_response("feeds/list.html", {
            "entries": paginator_page,
            }, context_instance=RequestContext(request)
                              )


                              
