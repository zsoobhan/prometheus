from django.utils.translation import ugettext as _
from django import forms

from . import models


class ContactForm(forms.ModelForm):

    robots_check_this = forms.BooleanField(
        required=False,
        widget=forms.HiddenInput)

    answer = forms.IntegerField(
        required=True,
        help_text="Answer the simple sum to prove you're human.",
        label="Answer")

    def clean_robots_check_this(self):
        # Only robots are likely to see this field.
        # You shall not pass!
        if self.cleaned_data.get('robots_check_this'):
            raise forms.ValidationError(
                _('This field is hidden, you must be a bot!'),
                code='robot')

    def clean_answer(self):
        # Validate the answer
        answer = self.cleaned_data.get('answer')
        if answer != self.calculated_answer:
            raise forms.ValidationError(
                _('The answer you entered is incorrect.'),
                code='incorrect_answer')

        return answer

    def __init__(self, *args, **kwargs):
        # Add answer from session to form instance
        self.calculated_answer = kwargs.pop('answer', None)
        super(ContactForm, self).__init__(*args, **kwargs)

    class Meta:
        model = models.Communication
        exclude = ['date_created']
