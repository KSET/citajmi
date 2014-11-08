# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from landing.forms import SkipForm


def landing_page(request):
    if request.method == 'POST':
        form = SkipForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['skip']:
                request.session['skip'] = True
            return redirect('myflatpages:home')
    else:
        form = SkipForm()
    return render(request, 'landing/landing.html', {
        'form': form,
    })
