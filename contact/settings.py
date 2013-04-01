# coding: utf-8
from django.conf import settings

EMAIL_SUBJECT_PREFIX = getattr(settings, 'CONTACT_EMAIL_SUBJECT_PREFIX', '[Citajmi] ')
RECIPIENTS_MAIL = getattr(settings, 'CONTACT_RECIPIENTS_MAIL', [])
