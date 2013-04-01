# -*- coding: utf-8 -*-
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from events.models import Event
from events.forms import EventForm, EventImgForm
from events.utils import send_mail_notification
import datetime
import time

def event_add(request):
    if request.method == 'POST':
        event_form = EventForm(request.POST)
        img_form = EventImgForm(request.POST, request.FILES)
        if event_form.is_valid() and img_form.is_valid():
            event = event_form.save()
            if 'image' in request.FILES:
                img = img_form.save(commit=False)
                img.event = event
                img.save()
            send_mail_notification(event)
            msg = u'Događaj je uspješno prijavljen. Bit će vidljiv nakon odobrenja urednika.'
            messages.add_message(request, messages.SUCCESS, msg)
            return redirect('events:event_list')
    else:
        event_form = EventForm()
        img_form = EventImgForm()

    return render(request, 'events/add.html', {
        'event_form': event_form,
        'img_form': img_form,
    })

def make_archive_links():
    """Make a list of months to show archive links."""
    if not Event.objects.exists(): return []
    # set up vars
    year, month = time.localtime()[:2]
    first = Event.objects.order_by('start')[0]
    fyear = first.start.year
    fmonth = first.start.month
    months = []
    # loop over years and months
    for y in range(year, fyear-1, -1):
        start, end = 12, 0
        if y == year: start = month
        if y == fyear: end = fmonth-1
        for m in range(start, end, -1):
            date = datetime.date(year=y, month=m, day=1)
            count = Event.objects.month(y, m).count()
            months.append((date, count))
    return months

def event_list(request):
    archive = 'a' in request.GET
    return render(request, 'events/list.html', {
        'archive': archive,
        'months': make_archive_links() if archive else [],
        'events': Event.objects.current(),
    })

def event_archive(request, year, month):
    try:
        date = datetime.date(year=int(year), month=int(month), day=1)
    except Exception:
        raise Http404
    return render(request, 'events/list.html', {
        'date': date,
        'archive': True,
        'months': make_archive_links(),
        'events': Event.objects.month(year, month),
    })

def event_detail(request, slug):
    event = get_object_or_404(Event, slug=slug)
    if not event.public:
        raise Http404
    archive = 'a' in request.GET
    return render(request, 'events/detail.html', {
        'archive': archive,
        'months': make_archive_links() if archive else [],
        'event': event,
    })
