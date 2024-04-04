from edc_constants.constants import YES
from edc_form_validators import FormValidator


class DeathReportFormValidator(FormValidator):

    def clean(self):

        self.validate_other_specify(
            field='death_cause',)

        self.validate_other_specify(
            field='cause_category',)

