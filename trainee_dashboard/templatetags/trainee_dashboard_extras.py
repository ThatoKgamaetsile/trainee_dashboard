from django import template
from django.conf import settings

register = template.Library()


@register.inclusion_tag('trainee_dashboard/buttons/screening_button.html')
def screening_button(model_wrapper):
    title = ['Add subject\' screening form.']
    return dict(
        screening_identifier=model_wrapper.object.screening_identifier,
        add_subject_screening_href=model_wrapper.subject_screening.href,
        subject_screening_model_obj=model_wrapper.subject_screening_model_obj,
        title=' '.join(title))


@register.inclusion_tag('trainee_dashboard/buttons/subject_locator_button.html')
def subject_locator_button(model_wrapper):
    title = ['Edit Locator.']
    return dict(
        subject_identifier=model_wrapper.subject_locator.subject_identifier,
        add_subject_locator_href=model_wrapper.subject_locator.href,
        subject_locator_model_obj=model_wrapper.subject_locator_model_obj,
        title=' '.join(title))


@register.inclusion_tag('trainee_dashboard/buttons/consent_button.html')
def consent_button(model_wrapper):
    title = ['Consent subject to participate.']
    return dict(
        screening_identifier=model_wrapper.object.screening_identifier,
        add_consent_href=model_wrapper.href,
        title=' '.join(title))


@register.inclusion_tag('trainee_dashboard/buttons/dashboard_button.html')
def dashboard_button(model_wrapper):
    subject_dashboard_url = settings.DASHBOARD_URL_NAMES.get(
        'subject_dashboard_url')
    return dict(
        subject_dashboard_url=subject_dashboard_url,
        subject_identifier=model_wrapper.subject_identifier)
