from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns(
    '',
    url(r'^$',
        views.BlogEntryListView.as_view(), name="blog-entry-list-view"),
    url(r'^(?P<slug>[-_\w]+)/$',
        views.BlogEntryDetailView.as_view(), name='blog-entry-detail-view'),
)
