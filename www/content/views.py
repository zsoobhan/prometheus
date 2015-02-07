from django.views import generic
from django.contrib import messages
from django.utils.translation import ugettext as _
from . import forms


class ContactFormView(generic.FormView):

    form_class = forms.ContactForm
    template_name = 'content/contact.html'
    success_url = '/'
    success_message = _("Your contact message has been saved and I will be in "
                        "touch shortly.")

    def form_valid(self, form):
        form.save()
        messages.success(self.request, self.success_message)
        return super(ContactFormView, self).form_valid(form)


class HomeView(generic.TemplateView):
    template_name = 'content/home.html'
