# -*- coding: utf-8 -*-
from django.conf import settings

EMAIL_SUBJECT = getattr(settings, 'EVENTS_EMAIL_SUBJECT', u'[Citajmi] Prijavljeni događaj zahtijeva odobrenje')
SENDER_MAIL = getattr(settings, 'EVENTS_SENDER_MAIL', 'no-reply@citajmi.info')
RECIPIENTS_MAIL = getattr(settings, 'EVENTS_RECIPIENTS_MAIL', [])
# site address, on wich is appended /admin/event/events/<id>/
# for generating link for admin approval
SITE_LINK = getattr(settings, 'EVENTS_SITE_LINK', 'http://www.citajmi.info')
# 1048576 = 1mb
IMG_MAX_SIZE = getattr(settings, 'EVENTS_IMG_MAX_SIZE', 1048576 * 2)
# allowed content_type without 'image/' part
IMG_TYPES = getattr(settings, 'EVENTS_IMG_TYPES', ['jpeg', 'png'])
