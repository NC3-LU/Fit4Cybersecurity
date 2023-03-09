import json
from typing import Any
from typing import Dict

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView

from audit.forms import ObservationsTextarea
from audit.forms import ReferencesTextarea
from audit.forms import SignUpForm
from audit.forms import StatusChoices
from audit.models import Audit
from audit.models import AuditByUser
from audit.models import AuditQuestion
from audit.models import AuditUser
from csskp.settings import CUSTOM
from survey.models import CONTEXT_SECTION_LABEL
from survey.models import SurveyQuestion
from survey.models import SurveyUser
from survey.models import SurveyUserAnswer
from survey.viewLogic import find_user_by_id
from survey.viewLogic import get_answered_questions_sequences


@login_required
def index(request):
    if request.method == "POST":
        body_unicode = request.body.decode("utf-8")
        body = json.loads(body_unicode)
        id = body.pop("id", None)
        Audit.objects.filter(id=id).update(**body)

    auditsByUser = []

    try:
        auditsByUser = request.user.audituser.get_all_audits()
    except AuditUser.DoesNotExist:
        pass

    for auditByUser in auditsByUser:
        auditByUser.statusForm = StatusChoices(
            id=auditByUser.audit.id,
            status=auditByUser.audit.status,
            type_of_company=auditByUser.audit_user.company.type,
        )

    context = {
        "auditsByUser": auditsByUser,
        "companies_admin": request.user.company_admin.all(),
    }

    return render(request, "index.html", context=context)


def signup(request):
    return render(request, "audit/signup.html")


@login_required
def audit(request, audit_id: int):
    auth_user_id = request.session.get("_auth_user_id", None)
    audit_by_user = AuditByUser.objects.filter(
        audit=audit_id, audit_user__user=auth_user_id
    )

    if auth_user_id is None or not audit_by_user:
        return HttpResponseRedirect("/audit")

    survey_user_id = Audit.objects.filter(id=audit_id).first().survey_user.user_id

    if survey_user_id is None:
        return HttpResponseRedirect("/audit")

    user = find_user_by_id(survey_user_id)
    type_of_company = AuditUser.objects.filter(user=auth_user_id).first().company.type

    if request.method == "POST":
        body_unicode = request.body.decode("utf-8")
        body = json.loads(body_unicode)
        id = body.pop("id", None)
        AuditQuestion.objects.filter(id=id).update(**body)

    audit_questions = AuditQuestion.objects.filter(
        survey_user__user_id=survey_user_id
    ).order_by("id")
    survey_user_answers = (
        SurveyUserAnswer.objects.filter(user=user, uvalue=1)
        .exclude(answer__question__section__label=CONTEXT_SECTION_LABEL)
        .order_by("answer__question__qindex", "answer__aindex")
    )

    if not audit_questions:
        answered_questions_sequences = get_answered_questions_sequences(user)
        audit_questions = AuditQuestion.objects.filter(
            survey_user__user_id=survey_user_id
        ).order_by("id")

        for answered_question_sequence in answered_questions_sequences:
            audit_question = AuditQuestion()
            audit_question.survey_question = SurveyQuestion.objects.filter(
                id=answered_question_sequence.question.id
            ).first()
            audit_question.survey_user = SurveyUser.objects.filter(
                user_id=survey_user_id
            ).first()
            audit_question.save()

    audit_questions_formatted: Dict[int, Any] = {}

    for index, audit_question in enumerate(audit_questions):
        audit_questions_formatted[index] = {
            "id": audit_question.id,
            "question": _(audit_question.survey_question.label),
            "answer": survey_user_answers.filter(
                answer__question__id=audit_question.survey_question.id
            ).values("answer__label"),
            "referenceForm": ReferencesTextarea(
                id=audit_question.id,
                reference=audit_question.references,
                type_of_company=type_of_company,
            ),
            "observationForm": ObservationsTextarea(
                id=audit_question.id,
                observation=audit_question.observations,
                type_of_company=type_of_company,
            ),
            "statusForm": StatusChoices(
                id=audit_question.id,
                status=audit_question.status,
                type_of_company=type_of_company,
            ),
        }

    context = {
        "title": CUSTOM["tool_name"] + " - " + _("Audit"),
        "audit_questions": audit_questions_formatted,
    }

    return render(request, "audit.html", context=context)


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("audit")
    template_name = "registration/signup.html"
