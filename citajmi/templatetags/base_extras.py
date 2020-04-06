from django import template
from django.core.urlresolvers import reverse
import re

register = template.Library()


@register.simple_tag
def search(string, pattern, result_true, result_false):
    if string and pattern and re.search(pattern, string):
        return result_true
    return result_false


# use for class=active in navbar
@register.simple_tag
def active(request, pattern):
    return search(request.path, pattern, result_true='active', result_false='') if request else ''


@register.simple_tag
def active_reverse(request, view_name):
    pattern = ''
    try:
        pattern = reverse(view_name)
    except Exception:
        pass
    return active(request, pattern)


@register.filter
def split(string, delimiter):
    return string.split(delimiter)
