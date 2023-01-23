from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from audit.globals import QUESTION_STATUS


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text="Optional")
    last_name = forms.CharField(max_length=30, required=False, help_text="Optional")
    email = forms.EmailField(max_length=254, help_text="Enter a valid email address")
    company = forms.CharField(max_length=254)

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "company",
            "password1",
            "password2",
        ]


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
