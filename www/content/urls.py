from django.conf.urls import patterns, url
from django.views import generic

urlpatterns = patterns(
    '',
    url(r'^$', generic.TemplateView.as_view(
        template_name="content/home.html")),
)
