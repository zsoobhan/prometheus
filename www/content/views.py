from django.views import generic
from django.contrib import messages
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse_lazy

from . import forms


class ContactFormView(generic.FormView):

    form_class = forms.ContactForm
    template_name = 'content/contact.html'
    success_url = reverse_lazy('home')
    success_message = _("Your contact message has been saved and I will be in "
                        "touch shortly.")

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
