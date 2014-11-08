# -*- coding: utf-8 -*-
from django import forms


class SkipForm(forms.Form):
    skip = forms.BooleanField(required=False, label=u'Preskoči ovu stranicu prilikom sljedećeg posjeta.')
