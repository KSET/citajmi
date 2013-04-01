# -*- coding: utf-8 -*-
from events import settings
from django.core.mail import send_mail

def send_mail_notification(event):
    subject = settings.EMAIL_SUBJECT
    sender = settings.SENDER_MAIL
    link = '%s/admin/events/event/%d/' % (settings.SITE_LINK, event.id)
    message = u"""Kao urednik stranice, potrebno je vaše odobrenje za
              prijavljeni događaj:

              Naziv: %s
              Lokacija: %s

              Kada vam odgovara, posjetite:

              %s
              da odobrite ili odbijete zahtjev.""" % (event.title, event.location, link)
    message = '\n'.join([line.strip() for line in message.split('\n')])
    recipients = settings.RECIPIENTS_MAIL
    try:
        send_mail(subject, message, sender, recipients)
    except Exception:
        pass
