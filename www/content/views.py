import datetime
import os

from django.conf import settings
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.utils.translation import ugettext as _
from django.views import generic


class ContactFormView(generic.TemplateView):
    template_name = "content/contact.html"


class HomeView(generic.TemplateView):
    template_name = "content/home.html"

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["years"] = datetime.date.today().year - 2012
        return context


class ResumeLandingView(generic.TemplateView):
    template_name = "content/resume.html"


class ResumeView(generic.View):
    def get(self, request, *args, **kwargs):
        filepath = os.path.join(settings.STATIC_ROOT, "docs/resume_zsoobhan.pdf")
        with open(filepath, "r") as pdf:
            response = HttpResponse(pdf.read(), content_type="application/pdf")
            response["Content-Disposition"] = "inline;filename=resume_zsoobhan.pdf"
            return response
