from django import template

register = template.Library()

# I have a feeling this is unnecessary.

@register.inclusion_tag("templatetags/stats.html")
def render_stats(stat_object):
    return stat_object


