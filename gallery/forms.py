# -*- coding: utf-8 -*-
from django import forms
from gallery.models import AlbumEntry, EntryImg
from gallery import settings
from gallery.templatetags.custom_filters import youtube_embed_url

class AlbumEntryForm(forms.ModelForm):

    def clean_full_name(self):
        return self.cleaned_data.get('full_name', '').strip()
    def clean_address(self):
        return self.cleaned_data.get('address', '').strip()
    def clean_video(self):
        data = self.cleaned_data.get('video', '')
        if data and not youtube_embed_url(data):
            raise forms.ValidationError('Provjerite da li je adresa video snimke ispravna.')
        return data

    def custom_is_valid(self, request):
        video = self.data.get('video', '')
        if not self.is_valid(): return False
        if not video and 'image' not in request.FILES:
            errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.util.ErrorList())
            errors.append(u'Morate poslati fotografiju ili video snimku.')
            return False
        if video and 'image' in request.FILES:
            errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.util.ErrorList())
            errors.append(u'Ne možete poslati fotografiju i video snimku u istom unosu.')
            return False
        return True

    class Meta:
        model = AlbumEntry
        exclude = ('cover', 'public', 'created')


class EntryImgForm(forms.ModelForm):
    help_text = 'Maks. veličina %dmb.' % (settings.IMG_MAX_SIZE/1048576)
    image = forms.ImageField(label=u'Fotografija', required=False, help_text=help_text)

    def clean_image(self):
        image = self.cleaned_data.get('image', None)
        if image:
            if image.content_type.replace('image/', '') not in settings.IMG_TYPES:
                raise forms.ValidationError('Fotografija mora biti u %s formatu.' % (' ili '.join(settings.IMG_TYPES),))
            if image._size > settings.IMG_MAX_SIZE:
                raise forms.ValidationError('Fotografija je prevelika ( > %dmb )' % (settings.IMG_MAX_SIZE/1048576))
        return image

    class Meta:
        model = EntryImg
        fields = ('image',)

class AcceptForm(forms.Form):
    accept = forms.BooleanField(required=True, label=u'Potvrđujem da sam autor fotografije/video snimke i dozvoljavam objavljivanje na internet stranicama kampanje "Čitaj mi!".')
