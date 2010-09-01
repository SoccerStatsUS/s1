from django import template

register = template.Library()


@register.inclusion_tag('templatetags/paginator.html', takes_context=True)
def easy_paginator(context, paginator):
        return {
            'query_string': ".?%s" % context['request'].META['QUERY_STRING'],
            'paginator': paginator,
            'MEDIA_URL': context.get('MEDIA_URL'),
                    }
    

# Splice kwargs into urls.
# Keep simple until you can't.

class GetUrlNode(template.Node):
    pass

def do_get_url(parser, token):
    pass

register.tag('get_url', do_get_url)
               
    
