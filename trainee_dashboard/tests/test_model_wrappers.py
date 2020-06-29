from django.test import TestCase, tag
from edc_model_wrapper.tests import ModelWrapperTestHelper
from ..model_wrappers import SubjectScreeningModelWrapper


class SubjectModelWrapperTestHelper(ModelWrapperTestHelper):
    dashboard_url = '/subject_dashboard/'


class ScreeningModelWrapperTestHelper(ModelWrapperTestHelper):
    dashboard_url = '/screening_listboard/'


class TestModelWrappers(TestCase):

    model_wrapper_helper_cls = SubjectModelWrapperTestHelper

    @tag('1')
    def test_subject_screening(self):
        helper = ScreeningModelWrapperTestHelper(
            model_wrapper=SubjectScreeningModelWrapper,
            app_label='trainee_dashboard',
            screening_identifier='ABCDEFGH')
        helper.test(self)