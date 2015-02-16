# -*- coding: utf-8 -*-
# custom context processors
from events.models import Event


def current_events(request):
    events = Event.objects.current()
    return {
        'current_events': events[:2],
    }
