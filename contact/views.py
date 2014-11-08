# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from contact import settings
from django.contrib import messages
from contact.forms import ContactForm
from django.core.mail import send_mail


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = settings.EMAIL_SUBJECT_PREFIX + form.cleaned_data['subject']
            sender = form.cleaned_data['sender']
            message = form.cleaned_data['message']
            recipients = settings.RECIPIENTS_MAIL
            try:
                send_mail(subject, message, sender, recipients)
                msg = u'Poruka je uspješno poslana.'
                messages.add_message(request, messages.SUCCESS, msg)
            except Exception:
                msg = u'Trenutačno se ne mogu slati poruke.'
                messages.add_message(request, messages.ERROR, msg)
            return redirect('contact:contact')
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {
        'form': form,
    })
