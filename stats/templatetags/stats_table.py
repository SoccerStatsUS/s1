from django import template

register = template.Library()

default_table_attrs = [("GP", "games_played"), 
                       ("GS", "games_started"),
                       ("Minutes", "minutes"),
                       ("Goals", "goals"),
                       ("Assists", "assists"),
                       ]


@register.inclusion_tag("templatetags/career_stats.html")
def render_career_stats(stat_list, table_attrs=None):
    if table_attrs is None:
        table_attrs = default_table_attrs
    return {
        "stat_list": stat_list,
        "table_attrs": table_attrs,
        }

@register.inclusion_tag("templatetags/individual_stats.html")
def render_individual_stats(stat_list, table_attrs=None):
    return render_career_stats(stat_list, table_attrs)

