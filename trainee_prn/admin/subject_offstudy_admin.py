from django.contrib import admin
from edc_base.modeladmin_mixins import audit_fieldset_tuple

from trainee_prn.admin.modeladmin_mixin import ModelAdminMixin

from ..admin_site import trainee_prn_admin
from ..forms import SubjectOffStudyForm
from ..models import SubjectOffStudy



@admin.register(SubjectOffStudy, site=trainee_prn_admin)
class SubjectOffStudyAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = SubjectOffStudyForm

    fieldsets = (
        ('Fields to be completed by Trainee Research Assistant (Deaths/LTFU)',
            {
                'fields': ('subject_identifier',
                           'report_datetime',
                           'offstudy_date',
                           'reason',
                           'reason_other',
                )
            }),
        audit_fieldset_tuple)

    radio_fields = {'reason': admin.VERTICAL, }

    search_fields = ('subject_identifier',)

    list_display = ('subject_identifier', 'offstudy_date',)