from django.views import generic
from django.http import Http404

from . import models


class BlogEntryListView(generic.ListView):
    template_name = 'blog/list.html'
    model = models.BlogEntry
    queryset = models.BlogEntry.objects.filter(status=models.PUBLISHED)
    context_object_name = 'active_blog_entries'
    paginate_by = 10
    queryset = models.BlogEntry.objects.all().prefetch_related('tags')

    def get_queryset(self):
        'return the active blog entries'
        queryset = super(BlogEntryListView, self).get_queryset()
        return [entry for entry in queryset if entry.is_active]


class BlogEntryDetailView(generic.DetailView):
    template_name = 'blog/detail.html'
    model = models.BlogEntry

    def get_object(self):
        blog_entry = super(BlogEntryDetailView, self).get_object()
        user = getattr(self.request, 'user')

        # return early if superuser
        if user and user.is_superuser:
            return blog_entry

        if not blog_entry.is_active:
            raise Http404('The blog entry requested is currently inactive.')

        return blog_entry
