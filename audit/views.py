import json
from typing import Any
from typing import Dict

from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render
from django.utils.translation import gettext as _

from audit.forms import AuditForm
from audit.forms import CompanyForm
from audit.forms import ObservationsTextarea
from audit.forms import ReferencesTextarea
from audit.forms import SignUpForm
from audit.forms import StatusChoices
from audit.forms import EditProduct
from audit.models import Audit
from audit.models import AuditByUser
from audit.models import AuditQuestion
from audit.models import AuditUser
from audit.models import Company
from csskp.settings import CUSTOM
from survey.models import CONTEXT_SECTION_LABEL
from survey.models import SurveyQuestion
from survey.models import SurveyUser
from survey.models import SurveyUserAnswer
from survey.viewLogic import find_user_by_id
from survey.viewLogic import get_answered_questions_sequences


@login_required
def index(request):
    """Index view of the audit module."""
    if request.method == "POST":
        body_unicode = request.body.decode("utf-8")
        body = json.loads(body_unicode)
        id = body.pop("id", None)
        Audit.objects.filter(id=id).update(**body)

    auditsByUser = []

    try:
        auditsByUser = request.user.audituser.get_all_audits()
    except request.user.audituser.DoesNotExist:
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
        "kind_of_company_label": _("Audit company")
        if request.user.audituser.company.type == "CS"
        else _("Client company"),
        "kind_of_company_label": _("Audit company")
        if request.user.audituser.company.type == "CS"
        else _("Client company"),
    }

    return render(request, "index.html", context=context)


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            clean_form = form.cleaned_data
            username = clean_form.get("username")
            raw_password = clean_form.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, "Your signed up successfully!")
            return redirect("/audit")
    else:
        form = SignUpForm()
    return render(request, "signup.html", {"form": form})


@login_required
def audit(request, audit_id: int):
    """Manage audits."""
    auth_user_id = request.session.get("_auth_user_id", None)
    audit_by_user = AuditByUser.objects.filter(
        audit=audit_id, audit_user__user=auth_user_id
    )

    if auth_user_id is None or not audit_by_user:
        return HttpResponseRedirect("/audit")

    survey_user_id = Audit.objects.filter(
        id=audit_id).first().survey_user.user_id

    if survey_user_id is None:
        return HttpResponseRedirect("/audit")

    user = find_user_by_id(survey_user_id)
    type_of_company = AuditUser.objects.filter(
        user=auth_user_id).first().company.type

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


@login_required
def edit_product(request, audit_id: int):
    if not request.user.audituser.auditbyuser_set.filter(audit_id=audit_id).exists():
        return HttpResponseRedirect("/audit")

    form = EditProduct(product=Audit.objects.get(id=audit_id))

    if request.method == "POST":
        form = EditProduct(data=request.POST,
                         product=Audit.objects.get(id=audit_id))

        if form.is_valid():
            audit = Audit.objects.get(id=audit_id)
            audit.product_name = form.cleaned_data["name"]
            audit.product_ref = form.cleaned_data["reference"]

            audit.auditbycompany_set.filter(audit_company__type="AD").update_or_create(
                audit_id=audit_id,
                defaults={
                    "audit_company_id": form.cleaned_data["company"].id,
                },
            )
            audit.save()

        return HttpResponseRedirect("/audit")

    return render(
        request, "edit_product.html", context={"form": form, "audit_id": audit_id}
    )


@login_required
def create_company(request):
    """View to create a company."""
    if request.method == "POST":
        form = CompanyForm(request.POST)
        if form.is_valid():
            form = CompanyForm(request.POST)
            new_company = form.save(False)
            new_company.company_admin_id = request.user.id
            new_company = form.save()
            new_company.members.set([request.user])
            new_company.save()
            return redirect(f"/audit/company/{new_company.id}")
    else:
        form = CompanyForm()
    return render(request, "edit_company.html", {"form": form})


@login_required
def edit_company(request, company_id=None):
    """View to edit a company."""
    company = Company.objects.get(id=company_id)
    if request.method == "POST":
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form = CompanyForm(request.POST, instance=company)
            form.save()
            return redirect(f"/audit/company/{company.id}")
    else:
        form = CompanyForm(instance=company)
    return render(request, "edit_company.html", {"form": form})


@login_required
def create_audit(request):
    """View to create an audit."""
    if request.method == "POST":
        form = AuditForm(request.POST)
        if form.is_valid():
            form = AuditForm(request.POST)
            new_audit = form.save(False)
            new_audit.save()
            return redirect(f"/audit/audit/{new_audit.id}")
    else:
        form = AuditForm()
    return render(request, "edit_audit.html", {"form": form})


@login_required
def edit_audit(request, audit_id=None):
    """View to create an audit."""
    audit = Audit.objects.get(id=audit_id)
    if request.method == "POST":
        pass
    else:
        form = AuditForm(instance=audit)
    return render(request, "edit_audit.html", {"form": form})
