from django.conf.urls import patterns, url
from . import views
urlpatterns = patterns(
    '',
    url(r'^$', views.HomeView.as_view(), name="home"),
    url(r'^contact/$', views.ContactFormView.as_view(), name="contact"),
    url(r'^infrastructure/$', views.InfrastructureView.as_view(), name="infrastructure"),
    url(r'^blog/$', views.BlogView.as_view(), name="blog"),
)
