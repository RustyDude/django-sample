from django import forms
from django.core.mail import EmailMessage

EMAIL_RECIPIENT_LIST = 'rustydude09@gmail.com'


class ContactForm(forms.Form):
    phone_invalid = "Phone number format must be :'+999999999'. Up to 15 digits allowed."

    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    phone = forms.RegexField(regex=r'^\+?1?\d{9,15}$', error_messages={'invalid': phone_invalid})
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        phone = form.cleaned_data['phone']
        message = form.cleaned_data['message']

        info = '{} <{}|{}>'.format(name, email, phone)
        email = EmailMessage(info, message, to=[EMAIL_RECIPIENT_LIST])
        email.send()
