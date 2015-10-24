from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView
from django.views.generic.edit import FormView

from .forms import ContactForm
from .models import UserProfile


class ProfileView(ListView):
    model = UserProfile
    template_name = "about.html"


class ContactView(SuccessMessageMixin, FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = reverse_lazy("profile:contact")
    success_message = "This message was sent successfully, I will try to get back to you as soon as possible!"

    def form_valid(self, form):
        form.send_email(form)
        return super(ContactView, self).form_valid(form)
