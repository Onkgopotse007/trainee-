from django.apps import AppConfig as DjangoAppConfig
from dateutil.relativedelta import MO, TU, WE, TH, FR, SA, SU
from edc_facility.apps import AppConfig as BaseEdcFacilityAppConfig
from edc_appointment.appointment_config import AppointmentConfig
from edc_appointment.apps import AppConfig as BaseEdcAppointmentAppConfig
from edc_visit_tracking.apps import AppConfig as BaseEdcVisitTrackingAppConfig
from edc_sms.apps import AppConfig as BaseEdcSmsAppConfig


class AppConfig(DjangoAppConfig):
    name = 'trainee_prn'
    verbose_name = 'Trainee PRN'
    admin_site_name = 'trainee_prn_admin'




class EdcFacilityAppConfig(BaseEdcFacilityAppConfig):
    country = 'botswana'
    definitions = {
        '7-day clinic': dict(days=[MO, TU, WE, TH, FR, SA, SU],
                             slots=[100, 100, 100, 100, 100, 100, 100]),
        '5-day clinic': dict(days=[MO, TU, WE, TH, FR],
                             slots=[100, 100, 100, 100, 100])
        }

class EdcAppointmentAppConfig(BaseEdcAppointmentAppConfig):
    send_sms_reminders = True
    apply_community_filter = True
    configurations = [
        AppointmentConfig(
            model='edc_appointment.appointment',
            related_visit_model='traineesubject.subjectvisit',
            appt_type='clinic')]


class EdcVisitTrackingAppConfig(BaseEdcVisitTrackingAppConfig):
    visit_models = {
        'traineesubject': ('subject_visit', 'traineesubject.subjectvisit')
        }


class EdcSmsAppConfig(BaseEdcSmsAppConfig):
    locator_model = 'traineesubject.subjectlocator'
    consent_model = 'traineesubject.subjectconsent'
