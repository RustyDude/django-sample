from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^markdown/', include("django_markdown.urls")),
    url(r'^', include('blog.urls', namespace='blog', app_name='blog')),
    url(r'^', include('userprofile.urls', namespace='profile', app_name='profile')),
]
