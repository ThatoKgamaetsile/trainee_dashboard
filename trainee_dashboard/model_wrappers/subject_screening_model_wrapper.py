from django.apps import apps as django_apps
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

from edc_model_wrapper import ModelWrapper

from .subject_locator_wrapper_mixin import subjectLocatorModelWrapperMixin


class SubjectScreeningModelWrapper(subjectLocatorModelWrapperMixin,
                                   ModelWrapper):

    model = 'trainee_subject.subjectscreening'
    querystring_attrs = ['screening_identifier']
    next_url_attrs = ['screening_identifier']
    next_url_name = settings.DASHBOARD_URL_NAMES.get('screening_dashboard_url')

    @property
    def subject_screening_model_obj(self):
        """Returns a subject screening model instance or None.
        """
        try:
            return self.subject_screening_cls.objects.get(
                **self.subject_screening_options)
        except ObjectDoesNotExist:
            return None

    @property
    def subject_identifier(self):
        if self.subject_screening_model_obj:
            return self.subject_screening_model_obj.subject_identifier
        return None

    @property
    def subject_screening_cls(self):
        return django_apps.get_model('trainee_subject.subjectscreening')

    @property
    def subject_screening(self):
        """Returns a wrapped saved or unsaved subject screening.
        """
        model_obj = self.subject_screening_model_obj or self.subject_screening_cls(
            **self.create_subject_screening_options)
        return SubjectScreeningModelWrapper(model_obj=model_obj)

    @property
    def create_subject_screening_options(self):
        """Returns a dictionary of options to create a new
        unpersisted trainee subject screening model instance.
        """
        options = dict(
            screening_identifier=self.screening_identifier)
        return options

    @property
    def subject_screening_options(self):
        """Returns a dictionary of options to get an existing
        subject screening model instance.
        """
        options = dict(
            screening_identifier=self.screening_identifier)
        return options
