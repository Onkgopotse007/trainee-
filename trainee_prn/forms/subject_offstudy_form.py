from django import forms
from edc_form_validators import FormValidatorMixin

from trainee_prn.form_validators.subject_offstudy_validator import SubjectOffstudyFormValidator

from ..models import SubjectOffStudy


class SubjectOffStudyForm(FormValidatorMixin, forms.ModelForm):

    form_validator_cls = SubjectOffstudyFormValidator

    class Meta:
        model = SubjectOffStudy
        fields = '__all__'
