import datetime
import os

from django.conf import settings
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.utils.translation import ugettext as _
from django.views import generic

from . import forms


class ContactFormView(generic.FormView):

    form_class = forms.ContactForm
    template_name = 'content/contact.html'
    success_url = reverse_lazy('home')
    success_message = _(
        "Your contact message has been saved and I will be in "
        "touch shortly."
    )

    def form_valid(self, form):
        form.save()
        messages.success(self.request, self.success_message)
        return super(ContactFormView, self).form_valid(form)

    def get_form_kwargs(self):
        # Adds answer from session to the form kwargs for human verification
        kwargs = super(ContactFormView, self).get_form_kwargs()
        kwargs['answer'] = self.request.session['q_and_a']['answer']
        return kwargs


class HomeView(generic.TemplateView):
    template_name = 'content/home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['years'] = datetime.date.today().year - 2012
        return context


class AboutView(generic.TemplateView):
    template_name = 'content/about.html'


class ResumeLandingView(generic.TemplateView):
    template_name = 'content/resume.html'


class ResumeView(generic.View):
    def get(self, request, *args, **kwargs):
        filepath = os.path.join(
            settings.STATIC_ROOT, 'docs/resume_zsoobhan.pdf'
        )
        with open(filepath, 'r') as pdf:
            response = HttpResponse(pdf.read(), content_type='application/pdf')
            response['Content-Disposition'
                     ] = 'inline;filename=resume_zsoobhan.pdf'
            return response
