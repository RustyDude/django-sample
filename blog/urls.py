from django.conf.urls import url

from .views import BlogIndex, BlogView

urlpatterns = [
    url(r'^$', BlogIndex.as_view(), name="index"),
    url(r'^blog/(?P<slug>\S+)$', BlogView.as_view(), name="page"),
]
