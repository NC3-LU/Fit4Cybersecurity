import json
from typing import Any
from typing import Dict
from uuid import UUID

from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render
from django.utils.translation import gettext as _

from audit.globals import QUESTION_STATUS
from audit.forms import AuditForm
from audit.forms import CompanyForm
from audit.forms import EditProduct
from audit.forms import ObservationsTextarea
from audit.forms import ReferencesTextarea
from audit.forms import SignUpForm
from audit.forms import StatusChoices
from audit.models import Audit
from audit.models import AuditQuestion
from audit.models import Certificate
from audit.models import Company
from audit.models import AuditByCompany
from audit.models import AuditByUser
from csskp.settings import CUSTOM
from survey.models import CONTEXT_SECTION_LABEL
from survey.viewLogic import get_answered_questions_sequences
from survey.viewLogic import find_user_by_id


@login_required
def index(request):
    """Index view of the audit module."""
    if request.method == "POST":
        body_unicode = request.body.decode("utf-8")
        body = json.loads(body_unicode)
        id = body.pop("id", None)
        Audit.objects.filter(id=id).update(**body)

    user = request.user

    if not user.auditbyuser_set.all():
        create_audit(request)

    auditsByUser = user.auditbyuser_set.all()
    filter_kind_of_company = "AD"
    if user.company_set.all().get().type == "AD":
        filter_kind_of_company = "CS"

    for auditByUser in auditsByUser:
        auditByUser.audit_company_selected = (
            auditByUser.audit.auditbycompany_set.filter(
                audit_company__type=filter_kind_of_company
            ).first()
        )
        auditByUser.audit.statusDetails = {}
        audit_questions = auditByUser.audit.survey_user.auditquestion_set.all()
        if audit_questions:
            for status in QUESTION_STATUS:
                auditByUser.audit.statusDetails[status[1]] = audit_questions.filter(
                    status=status[0]
                ).count()

    for auditByUser in auditsByUser:
        auditByUser.statusForm = StatusChoices(
            id=auditByUser.audit.id,
            status=auditByUser.audit.status,
            type_of_company=auditByUser.user.company_set.all().get().type,
        )

    context = {
        "auditsByUser": auditsByUser,
        "companies_admin": request.user.company_admin.all(),
        "kind_of_company_label": _("Audit company")
        if request.user.company_set.all().get().type == "CS"
        else _("Client company"),
    }

    return render(request, "index.html", context=context)


def signup(request):
    if request.method == "POST":
        formSignUp = SignUpForm(request.POST)
        formCompany = CompanyForm(request.POST)
        if formSignUp.is_valid() and formCompany.is_valid():
            new_user = formSignUp.save()
            new_company = formCompany.save(False)
            new_company.type = "CS"
            new_company.company_admin_id = new_user.id
            new_company.save()
            new_company.members.set([new_user])
            clean_formSignUp = formSignUp.cleaned_data
            username = clean_formSignUp.get("username")
            raw_password = clean_formSignUp.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, "Your signed up successfully!")
            return redirect("/audit")
    else:
        formSignUp = SignUpForm()
        formCompany = CompanyForm()
    return render(
        request, "signup.html", {
            "formSignUp": formSignUp, "formCompany": formCompany}
    )


@login_required
def audit(request, audit_id: int):
    """Manage audits."""
    try:
        user = request.user
        auditbyuser = user.auditbyuser_set.get(audit_id=audit_id)
        survey_user = auditbyuser.audit.survey_user
        type_of_company = request.user.company_set.all().get().type
    except ObjectDoesNotExist:
        return HttpResponseRedirect("/audit")

    if request.method == "POST":
        body_unicode = request.body.decode("utf-8")
        body = json.loads(body_unicode)
        id = body.pop("id", None)
        AuditQuestion.objects.filter(id=id).update(**body)

    if not survey_user.auditquestion_set.all().order_by("id").exists():
        answered_questions_sequences = get_answered_questions_sequences(
            survey_user)

        for answered_question_sequence in answered_questions_sequences:
            audit_question = AuditQuestion()
            audit_question.survey_question = answered_question_sequence.question
            audit_question.survey_user = answered_question_sequence.user
            audit_question.save()

    audit_questions = survey_user.auditquestion_set.all().order_by("id")
    survey_user_answers = (
        survey_user.surveyuseranswer_set.filter(uvalue=1)
        .exclude(answer__question__section__label=CONTEXT_SECTION_LABEL)
        .order_by("answer__question__qindex", "answer__aindex")
    )
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
    user = request.user

    if not user.auditbyuser_set.filter(audit_id=audit_id).exists():
        return HttpResponseRedirect("/audit")

    form = EditProduct(product=Audit.objects.get(id=audit_id))

    if request.method == "POST":
        if user.company_set.all().get().type == "AD":
            return HttpResponseRedirect("/audit")

        form = EditProduct(data=request.POST,
                           product=Audit.objects.get(id=audit_id))

        if form.is_valid():
            audit = Audit.objects.get(id=audit_id)
            audit.product_name = form.cleaned_data["name"]
            audit.product_ref = form.cleaned_data["reference"]

            if form.cleaned_data["company"]:
                audit.auditbycompany_set.filter(
                    audit_company__type="AD"
                ).update_or_create(
                    audit_id=audit_id,
                    defaults={
                        "audit_company_id": form.cleaned_data["company"].id,
                    },
                )
                audit.auditbyuser_set.filter(user__company__type="AD").update_or_create(
                    audit_id=audit_id,
                    defaults={
                        "user_id": form.cleaned_data["company"].company_admin_id,
                    },
                )
            else:
                audit.auditbycompany_set.filter(
                    audit_company__type="AD").delete()
                audit.auditbyuser_set.filter(user__company__type="AD").delete()

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
            new_certificate = Certificate()
            new_certificate.save()
            survey_user = find_user_by_id(
                UUID(form.cleaned_data["survey_user_uuid"]))
            new_audit = form.save(False)
            new_audit.certificate_id = new_certificate.id
            new_audit.survey_user_id = survey_user.id
            new_audit.save()
            new_auditbycompany = AuditByCompany(False)
            new_auditbycompany.audit_id = new_audit.id
            new_auditbycompany.audit_company_id = (
                request.user.company_set.all().get().id
            )
            new_auditbycompany.save()
            new_auditbyuser = AuditByUser(False)
            new_auditbyuser.audit_id = new_audit.id
            new_auditbyuser.user_id = request.user.id
            new_auditbyuser.save()

            return HttpResponseRedirect("/audit")
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


@login_required
def companies_list(request):
    """View of companies list"""
    companies = Company.objects.filter(type="AD")
    return render(request, "companies_list.html", {"companies": companies})