from django import forms


class ContactForm(forms.Form):
    # custom css class for jQuery selector
    CUSTOM_CLASS = 'contact-form-input'
    subject = forms.CharField(
        label=u'Naslov',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': u'Naslov', 'class': CUSTOM_CLASS})
    )
    sender = forms.EmailField(
        label=u'Email',
        widget=forms.TextInput(attrs={'placeholder': u'Email', 'class': CUSTOM_CLASS})
    )
    message = forms.CharField(
        label=u'Poruka',
        widget=forms.Textarea(attrs={'placeholder': u'Poruka', 'rows': 15, 'class': CUSTOM_CLASS})
    )
