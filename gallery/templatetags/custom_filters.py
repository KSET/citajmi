from django import template
from django.template.defaultfilters import stringfilter
import re

register = template.Library()


@register.filter
# converts youtube URL into embed URL
def youtube_embed_url(url):
    match = re.search(r'^(http|https)\:\/\/www\.youtube\.com\/watch[\/]?\?(.*)v\=(?P<id>[^&]*)(.*)$', url)
    if match:
        embed_url = 'http://www.youtube.com/embed/%s' % (match.group('id'),)
        return embed_url
    return ''


youtube_embed_url.is_safe = True


@register.filter
@stringfilter
# converts youtube URL into thumbnail pic URL
def youtube_thumbnail_url(url, big=True):
    match = re.search(r'^(http|https)\:\/\/www\.youtube\.com\/watch[\/]?\?(.*)v\=(?P<id>[^&]*)(.*)$', url)
    if match:
        thumbnail_url = 'http://img.youtube.com/vi/%s/%d.jpg' % (match.group('id'), 0 if big else 2)
        return thumbnail_url
    return ''


youtube_thumbnail_url.is_safe = True
