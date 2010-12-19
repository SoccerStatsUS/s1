import re

from django import template
from django.conf import settings


register = template.Library()

is_number = re.compile('^\d+$')

def getattribute(value, arg):
    if hasattr(value, arg):
        return getattr(value, arg)
    elif hasattr(value, 'get') and arg in value:
        return value[arg]
    elif is_number.match(arg):
        return value[int(arg)]
    else:
        return settings.TEMPLATE_STRING_IF_INVALID

register.filter('getattribute', getattribute)
