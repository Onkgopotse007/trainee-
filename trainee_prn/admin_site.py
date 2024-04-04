from django.contrib.admin import AdminSite as DjangoAdminSite


class AdminSite(DjangoAdminSite):
    site_title = 'Trainee PRN'
    site_header = 'Trainee PRN'
    index_title = 'Trainee PRN'
    site_url = '/administration/'


trainee_prn_admin = AdminSite(name='trainee_prn_admin')
