from edc_action_item import Action, HIGH_PRIORITY, site_action_items

DEATH_REPORT_ACTION = 'submit-death-report'
SUBJECT_OFFSTUDY_ACTION = 'submit-subject-offstudy'

class DeathReportAction(Action):
    name = DEATH_REPORT_ACTION
    display_name = 'Submit Death Report'
    reference_model = 'trainee_prn.deathreport'
    show_on_dashboard = True
    show_link_to_add = True
    priority = HIGH_PRIORITY
    singleton=True



class SubjectOffStudyAction(Action):
    name = SUBJECT_OFFSTUDY_ACTION
    display_name = 'Submit Subject Offstudy'
    reference_model = 'trainee_prn.subjectoffstudy'
    show_on_dashboard = True
    show_link_to_add = True
    priority = HIGH_PRIORITY
    singleton=True

site_action_items.register(DeathReportAction)
site_action_items.register(SubjectOffStudyAction)

