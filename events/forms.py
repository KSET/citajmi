# -*- coding: utf-8 -*-
from django import forms
from events.models import Event, EventImg
from events import settings


class EventForm(forms.ModelForm):

    def clean_title(self):
        return self.cleaned_data.get('title', '').strip()

    def clean_org(self):
        return self.cleaned_data.get('org', '').strip()

    def clean_location(self):
        return self.cleaned_data.get('location', '').strip()

    def clean_info(self):
        return self.cleaned_data.get('info', '').strip()

    def clean(self):
        cleaned_data = super(EventForm, self).clean()
        start = cleaned_data.get('start')
        end = cleaned_data.get('end')
        if start and end and (end - start).total_seconds() < 0:
            raise forms.ValidationError('Početak mora biti prije kraja događaja.')
        return cleaned_data

    class Meta:
        model = Event
        exclude = ('public', 'created')
        widgets = {
            'email': forms.TextInput(attrs={'placeholder': u'Neće biti vidljiv na stranici'}),
        }


class EventImgForm(forms.ModelForm):
    help_text = 'Maks. veličina %dmb. Slika nije obavezna.' % (settings.IMG_MAX_SIZE / 1048576)
    image = forms.ImageField(label=u'Slika uz događaj', required=False, help_text=help_text)

    def clean_image(self):
        image = self.cleaned_data.get('image', None)
        if image:
            if image.content_type.replace('image/', '') not in settings.IMG_TYPES:
                raise forms.ValidationError('Slika mora biti u %s formatu.' % (' ili '.join(settings.IMG_TYPES),))
            if image._size > settings.IMG_MAX_SIZE:
                raise forms.ValidationError('Slika je prevelika ( > %dmb )' % (settings.IMG_MAX_SIZE / 1048576))
        return image

    class Meta:
        model = EventImg
        fields = ('image',)
