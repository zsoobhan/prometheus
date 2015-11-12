from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns(
    '',
    url(r'^$', views.HomeView.as_view(), name="home"),
    url(r'^contact/$', views.ContactFormView.as_view(), name="contact"),
)
