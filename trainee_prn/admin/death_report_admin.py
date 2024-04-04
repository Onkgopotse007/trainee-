from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple
from trainee_prn.admin.modeladmin_mixin import ModelAdminMixin
from ..admin_site import trainee_prn_admin
from ..forms import DeathReportForm
from ..models import DeathReport



@admin.register(DeathReport, site=trainee_prn_admin)
class DeathReportAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = DeathReportForm

    search_fields = ('subject_identifier',)

    fieldsets = (
        (None, {
            'fields': [
                'subject_identifier',
                'report_datetime',
                'death_date',
                'info_source',
                'death_cause',
                'cause_other',
                'cause_category',
                'cause_category_other',
                'comment', ]}
         ), audit_fieldset_tuple)

    radio_fields = {
        'info_source': admin.VERTICAL,
        'cause_category': admin.VERTICAL,
         }
