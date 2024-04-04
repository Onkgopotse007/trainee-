from django import forms
from django.apps import apps as django_apps
from edc_constants.constants import YES
from edc_form_validators import FormValidator


class SubjectOffstudyFormValidator(FormValidator):

    def clean(self):
        super().clean()

        self.validate_other_specify(
            field='reason',
            other_specify_field='reason_other',
        )