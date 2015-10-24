from django.conf.urls import url

from .views import ContactView, ProfileView

urlpatterns = [
    url(r'^about-me/$', ProfileView.as_view(), name="index"),
    url(r'^contact/$', ContactView.as_view(), name="contact"),
]
