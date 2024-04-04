from django.db import models
from edc_action_item.model_mixins import ActionModelMixin
from edc_base.model_fields import OtherCharField
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators import date_not_future
from edc_base.model_validators import datetime_not_future
from edc_base.sites.managers import CurrentSiteManager
from edc_base.sites.site_model_mixin import SiteModelMixin
from edc_base.utils import get_utcnow
from edc_identifier.managers import SubjectIdentifierManager
from edc_protocol.validators import datetime_not_before_study_start

from ..action_items import DEATH_REPORT_ACTION
from ..choices import DEATH_INFO_SOURCE,CAUSE_OF_DEATH_CAT


class DeathReport(SiteModelMixin, ActionModelMixin, BaseUuidModel):

    action_name = DEATH_REPORT_ACTION

    tracking_identifier_prefix = 'DR'

    report_datetime = models.DateTimeField(
        verbose_name='Report Date',
        validators=[
            datetime_not_before_study_start,
            datetime_not_future],
        default=get_utcnow,
        help_text=('If reporting today, use today\'s date/time, otherwise use'
                   ' the date/time this information was reported.'))

    death_date = models.DateField(
        validators=[date_not_future],
        verbose_name='Date of Death:')

    info_source = models.CharField(
        max_length=50,
        choices=DEATH_INFO_SOURCE,
        verbose_name=('What was the source of information about participant'
                      'death?'
                      ))
    
    death_cause = models.TextField(
        verbose_name=('Describe the major cause of death (including pertinent'
                      ' autopsy information if available), starting with the'
                      ' first noticeable illness thought to be  related to'
                      ' death, continuing to time of death.'),
        blank=True,
        null=True,
        help_text=('Note: Cardiac and pulmonary arrest are not major reasons'
                   ' and should not be used to describe major cause'))
    
    cause_other = OtherCharField(
        max_length=50)

    cause_category = models.CharField(
        max_length=50,
        choices=CAUSE_OF_DEATH_CAT,
        verbose_name=('Based on the description above, what category'
                      ' best defines the major cause of death?'))

    cause_category_other = OtherCharField()

    comment = models.TextField(
        max_length=250,
        verbose_name='Comments',
        blank=True,
        null=True)

    def __str__(self):
        return f'{self.subject_identifier}'

    def natural_key(self):
        return (self.subject_identifier,)

    natural_key.dependencies = ['sites.Site']

    on_site = CurrentSiteManager()

    objects = SubjectIdentifierManager()

    history = HistoricalRecords()

    class Meta:
        app_label = 'trainee_prn'
        verbose_name = 'Death Report'
    
    

    