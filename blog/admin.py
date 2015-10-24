from django.contrib import admin

from django_markdown.admin import MarkdownModelAdmin

from .models import Entry, Tag


class EntryAdmin(MarkdownModelAdmin):
    list_display = ("title", "created", "modified")
    exclude = ['author', 'slug']

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()

admin.site.register(Entry, EntryAdmin)
admin.site.register(Tag)
