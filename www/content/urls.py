from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns(
    '',
    url(r'^$', views.HomeView.as_view(), name="home"),
    url(r'^contact/$', views.ContactFormView.as_view(), name="contact"),
    url(r'^about/$', views.AboutView.as_view(), name="about"),
    url(r'^resume/$', views.ResumeLandingView.as_view(), name="resume-landing"),
    url(r'^resume.pdf$', views.ResumeView.as_view(), name="resume"),
)
