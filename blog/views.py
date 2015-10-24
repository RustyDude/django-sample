from django.views.generic import DetailView, ListView

from .models import Entry


class BlogIndex(ListView):
    queryset = Entry.objects.published()
    template_name = "home.html"
    paginate_by = 3


class BlogView(DetailView):
    model = Entry
    template_name = "blog_page.html"
