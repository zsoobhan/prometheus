from django.utils.translation import ugettext as _
from django import forms

from . import models
from . import service


class ContactForm(forms.ModelForm):

    class Meta:
        model = models.Communication
        exclude = ['date_created']

    robots_check_this = forms.BooleanField(
        required=False,
        widget=forms.HiddenInput)

    answer = forms.IntegerField(
        required=True,
        # need to override __init__() to make this change
        # at run time
        label="What is %s + %s?" % service.generate_words())

    def clean_robots_check_this(self):
        # Only robots are likely to see this field.
        # You shall not pass!
        if self.cleaned_data.get('robots_check_this'):
            raise forms.ValidationError(
                _('This field is hidden, you must be a bot!'),
                code='robot')

    def clean_answer(self):
        # Validate the answer
        question = self.fields.get('answer').label
        calculated_answer = service.generate_answer(question)
        answer = self.cleaned_data.get('answer')

        if answer != calculated_answer:
            raise forms.ValidationError(
                _('The answer you entered is incorrect.'),
                code='incorrect_answer')

        return answer
