# -*- coding: utf-8 -*-
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from gallery.models import Album, AlbumEntry, EntryImg
from gallery.forms import AlbumEntryForm, EntryImgForm, AcceptForm
from django.utils import timezone
from datetime import date

def album_list(request):
    year = timezone.now().year
    return album_archive(request, year)

#! not a view
def make_archive_links():
    years = []
    qs = Album.objects.filter(public=True).order_by('date')
    if qs.exists():
        years.append(qs[0].date.year)
    else:
        years.append(timezone.now().year)
    for y in range(years[0] +1, timezone.now().year +1):
        years.append(y)
    return years

def album_archive(request, year):
    year = int(year)
    albums = Album.objects.filter(public=True, date__year=year)
    album_dict = {}
    for a in albums:
        album_dict.setdefault(a.date.month, []).append(a)
    archive = []
    for k, v in album_dict.items():
        archive.append({'month': date(year=year, month=k, day=1), 'albums': v})

    return render(request, 'gallery/list.html', {
        'archive': archive,
        'year': year,
        'years': make_archive_links(),
    })

def album_detail(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    if not album.public:
        raise Http404
    return render(request, 'gallery/detail.html', {
        'album': album,
        'year': album.date.year,
        'years': make_archive_links(),
    })

def entry_add(request):
    if request.method == 'POST':
        accept_form = AcceptForm(request.POST)
        entry_form = AlbumEntryForm(request.POST)
        img_form = EntryImgForm(request.POST, request.FILES)
        if accept_form.is_valid() and entry_form.custom_is_valid(request) and img_form.is_valid():
            entry = entry_form.save()
            if 'image' in request.FILES:
                img = img_form.save(commit=False)
                img.entry = entry
                img.save()
                msg = u'Fotografija je uspješno poslana.'
            else:
                msg = u'Video snimka je uspješno poslana.'
            messages.add_message(request, messages.SUCCESS, msg)
            return redirect('myflatpages:contest_prize')
    else:
        accept_form = AcceptForm(initial={'accept': True})
        entry_form = AlbumEntryForm()
        img_form = EntryImgForm()

    return render(request, 'gallery/add.html', {
        'entry_form': entry_form,
        'img_form': img_form,
        'accept_form': accept_form,
    })
