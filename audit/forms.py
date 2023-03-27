from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from audit.globals import QUESTION_STATUS
from audit.models import Audit
from audit.models import Company


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]


class CompanyForm(forms.ModelForm):
    name = forms.CharField(max_length=30, required=True)
    address_street = forms.CharField(max_length=30, required=True)
    address_zip_code = forms.CharField(max_length=30, required=True)
    address_city = forms.CharField(max_length=30, required=True)
    phone = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = Company
        fields = [
            "name",
            "address_street",
            "address_zip_code",
            "address_city",
            "phone",
            "email",
        ]


class AuditForm(forms.ModelForm):
    product_name = forms.CharField(max_length=30, required=True, label="Name")
    survey_user_uuid = forms.UUIDField(required=True, label="Self-assessment id")

    class Meta:
        model = Audit
        fields = ["product_name"]


class ReferencesTextarea(forms.Form):
    def __init__(self, *args, **kwargs):
        id_audit_question = kwargs.pop("id")
        reference = kwargs.pop("reference")
        type_of_company = kwargs.pop("type_of_company")
        super().__init__(*args, **kwargs)

        self.fields["references"] = forms.CharField(
            widget=forms.Textarea(
                attrs={
                    "id": id_audit_question,
                    "rows": 6,
                    "class": "w-100 h-100 border-0 bg-transparent",
                    "placeholder": "",
                    "onblur": "onBlurTextarea(this)",
                }
            ),
            disabled=True if type_of_company == "AD" else False,
            initial=reference,
        )


class ObservationsTextarea(forms.Form):
    def __init__(self, *args, **kwargs):
        id_audit_question = kwargs.pop("id")
        observation = kwargs.pop("observation")
        type_of_company = kwargs.pop("type_of_company")
        super().__init__(*args, **kwargs)

        self.fields["observations"] = forms.CharField(
            widget=forms.Textarea(
                attrs={
                    "id": id_audit_question,
                    "rows": 6,
                    "class": "w-100 h-100 border-0 bg-transparent",
                    "placeholder": "",
                    "onblur": "onBlurTextarea(this)",
                }
            ),
            disabled=True if type_of_company == "CS" else False,
            initial=observation,
        )


class StatusChoices(forms.Form):
    def __init__(self, *args, **kwargs):
        id_audit_question = kwargs.pop("id")
        status = kwargs.pop("status")
        type_of_company = kwargs.pop("type_of_company")
        super().__init__(*args, **kwargs)

        self.fields["status"] = forms.ChoiceField(
            choices=QUESTION_STATUS,
            widget=forms.Select(
                attrs={
                    "id": id_audit_question,
                    "class": "w-100 border-0 p-0 bg-transparent",
                    "onchange": "onChangeSelect(this)",
                }
            ),
            disabled=True if type_of_company == "CS" else False,
            initial=status,
        )


class EditProduct(forms.Form):
    name = forms.CharField(max_length=50)
    company = forms.ModelChoiceField(
        queryset=None, required=False, label="Audit company"
    )

    def __init__(self, *args, **kwargs):
        product = kwargs.pop("product", None)
        initialCompany = None
        if product.auditbycompany_set.filter(audit_company__type="AD").exists():
            initialCompany = (
                product.auditbycompany_set.filter(audit_company__type="AD")
                .first()
                .audit_company
            )

        super().__init__(*args, **kwargs)
        self.fields["name"].initial = product.product_name
        self.fields["company"].queryset = Company.objects.filter(
            type="AD", is_active=True
        )
        self.fields["company"].initial = initialCompany
        if product.auditbycompany_set.filter(audit_company__type="AD"):
            self.fields["company"].widget = forms.HiddenInput()
