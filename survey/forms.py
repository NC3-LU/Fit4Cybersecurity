from django import forms

from survey.globals import SECTOR_CHOICES, COMPANY_SIZE, TRANSLATION_UI, COUNTRIES
from survey.models import SurveyQuestionAnswer, TranslationKey
from django_countries.fields import CountryField


def sort_tuple_alphabetically(tuple, elementNumber):
    tuple.sort(key=lambda x: x[elementNumber])

    return tuple


class InitialStartForm(forms.Form):
    sector = forms.ChoiceField(required=True, widget=forms.Select)
    compSize = forms.ChoiceField(
        required=True, widget=forms.Select, choices=COMPANY_SIZE
    )

    def __init__(self, translations=None, *args, **kwargs):
        lang = kwargs.pop("lang")

        super().__init__(*args, **kwargs)

        self.fields["sector"].label = TRANSLATION_UI["form"]["start_form"][
            "sector_question"
        ][lang]
        sectors = []
        for sector_choise in SECTOR_CHOICES:
            sectors.append(
                (
                    sector_choise[0],
                    TRANSLATION_UI["form"]["start_form"]["sector_list"][
                        sector_choise[0]
                    ][lang],
                )
            )

        self.fields["sector"].choices = sort_tuple_alphabetically(sectors, 1)
        self.fields["compSize"].label = TRANSLATION_UI["form"]["start_form"][
            "size_question"
        ][lang]

        country_label = TRANSLATION_UI["form"]["start_form"]["country"]["label"][lang]
        required_error_message = TRANSLATION_UI["form"]["start_form"]["country"][
            "required_error_message"
        ][lang.lower()]
        self.fields["country"] = CountryField().formfield(
            label=country_label,
            required=True,
            initial="LU",
            error_messages={"required": required_error_message},
        )
        self.fields["country"].choices = COUNTRIES


class AnswerMChoice(forms.Form):
    unique_answers = forms.CharField(widget=forms.HiddenInput(), required=False)
    free_text_answer_id = forms.CharField(widget=forms.HiddenInput(), required=False)

    def __init__(self, tanswers=None, *args, **kwargs):
        self.lang = kwargs.pop("lang")
        answers_field_type = kwargs.pop("answers_field_type")
        self.question_type = answers_field_type
        question_answers = kwargs.pop("question_answers")
        data = kwargs.get("data")

        super().__init__(*args, **kwargs)

        if answers_field_type[0] == "M":
            self.fields["answers"] = forms.MultipleChoiceField(
                required=True,
                choices=[],
                widget=forms.CheckboxSelectMultiple(
                    attrs={"class": "multiple-selection"}
                ),
                label="",
            )
        elif answers_field_type[0] == "S":
            self.fields["answers"] = forms.ChoiceField(
                required=True,
                choices=[],
                widget=forms.RadioSelect(attrs={"class": "radio-buttons"}),
                label="",
            )
        elif answers_field_type == "T":
            self.fields["answers"] = forms.ChoiceField(
                required=True,
                choices=[],
                widget=forms.RadioSelect(attrs={"class": "radio-buttons"}),
                label="",
                initial=tanswers[0][0],
            )

        self.fields["answers"].error_messages = {
            "required": TRANSLATION_UI["form"]["error_messages"]["answer"]["required"][
                self.lang
            ]
        }

        if tanswers is not None:
            self.fields["answers"].choices = tanswers

        for question_answer in question_answers:
            if question_answer.atype == "T":
                isAnswerContentRequired = False
                if data is not None and data["free_text_answer_id"] != 0:
                    selected_answers = data["answers"]
                    if answers_field_type[0] == "S":
                        selected_answers = [data["answers"]]
                    if data["free_text_answer_id"] in selected_answers:
                        isAnswerContentRequired = True

                self.fields["answer_content"] = forms.CharField(
                    label="",
                    widget=forms.Textarea(
                        attrs={
                            "placeholder": "",
                        }
                    ),
                    required=isAnswerContentRequired,
                )

        self.fields["feedback"] = forms.CharField(
            label=TRANSLATION_UI["form"]["questions"]["feedback_label"][self.lang],
            widget=forms.Textarea(
                attrs={
                    "placeholder": TRANSLATION_UI["form"]["questions"][
                        "feedback_placeholder"
                    ][self.lang]
                }
            ),
            required=False,
        )

    def set_unique_answers(self, unique_answers_ids):
        self.fields["unique_answers"].initial = unique_answers_ids

    def set_free_text_answer_id(self, answer_id):
        self.fields["free_text_answer_id"].initial = answer_id

    def set_answers(self, answers_ids):
        if self.question_type != "T":
            self.fields["answers"].initial = answers_ids

    def clean_answers(self):
        answers = self.cleaned_data["answers"]

        if self.fields["answers"].widget.input_type == "radio":
            answers = [answers]

        if len(answers) > 1:
            unique_answer = SurveyQuestionAnswer.objects.filter(
                pk__in=answers, uniqueAnswer=1
            )
            if unique_answer.count():
                translation_key = TranslationKey.objects.filter(
                    lang=self.lang, key=unique_answer[0].answerKey
                )
                answer_text = translation_key[0].text

                raise forms.ValidationError(
                    TRANSLATION_UI["form"]["error_messages"]["answer"]["unique"][
                        self.lang
                    ],
                    params={"value": answer_text},
                )

        return answers

    def set_answer_content(self, answer_content):
        self.fields["answer_content"].initial = answer_content

    def set_feedback(self, feedback):
        self.fields["feedback"].initial = feedback


class GeneralFeedback(forms.Form):
    def __init__(self, *args, **kwargs):
        lang = kwargs.pop("lang")

        super().__init__(*args, **kwargs)

        self.fields["general_feedback"] = forms.CharField(
            label=TRANSLATION_UI["report"]["general_feedback"]["label"][lang],
            widget=forms.Textarea(
                attrs={
                    "placeholder": TRANSLATION_UI["report"]["general_feedback"][
                        "placeholder"
                    ][lang]
                }
            ),
            required=True,
        )

    def set_general_feedback(self, feedback):
        self.fields["general_feedback"].initial = feedback
