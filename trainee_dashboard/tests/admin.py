from django.contrib.admin import AdminSite as DjangoAdminSite

from .models import SubjectConsent, SubjectLocator
from .models import SubjectRequisition, SubjectVisit, SubjectScreening


class AdminSite(DjangoAdminSite):
    site_title = 'Trainee Subject'
    site_header = 'Trainee Subject'
    index_title = 'Trainee Subject'
    site_url = '/administration/'


trainee_test_admin = AdminSite(name='trainee_test_admin')

trainee_test_admin.register(SubjectScreening)
trainee_test_admin.register(SubjectConsent)
trainee_test_admin.register(SubjectLocator)
trainee_test_admin.register(SubjectVisit)
trainee_test_admin.register(SubjectRequisition)
