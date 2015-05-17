from django.conf import settings
from django.contrib import admin
from django.conf.urls import patterns, include, url
from django.views import generic


admin.autodiscover()

urlpatterns = patterns(
    '',
    (r'^admin/', include(admin.site.urls)),
    (r'^blog/', include('blog.urls')),
    (r'', include('content.urls')),
)

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    import debug_toolbar

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    urlpatterns += patterns(
        '',
        url(r'^404/$', generic.TemplateView.as_view(
            template_name='404.html'), name="404"),
        url(r'^500/$', generic.TemplateView.as_view(
            template_name='500.html'), name="500"),
        url(r'^__debug__/', include(debug_toolbar.urls)))
