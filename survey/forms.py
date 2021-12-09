# -*- coding: utf-8 -*-

from django import forms
from django.utils.translation import gettext_lazy as _
from survey.models import SurveyQuestionAnswer
import json


def sort_tuple_alphabetically(tuple, elementNumber):
    tuple.sort(key=lambda x: x[elementNumber])

    return tuple


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
            "required": _("You need to choose at least one answer")
        }

        if tanswers is not None:
            self.fields["answers"].choices = tanswers

        answers_dependencies = []
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
                            "autofocus": True,
                        }
                    ),
                    required=isAnswerContentRequired,
                )
            dependant_answers = question_answer.dependant_answers.all()
            if dependant_answers:
                answers_dependencies.append(
                    {
                        "leadId": question_answer.id,
                        "dependantIds": [
                            dep_answer.id for dep_answer in dependant_answers
                        ],
                    }
                )
                self.fields["answers"].widget.attrs["data-dependant-ids"] = json.dumps(
                    answers_dependencies
                )

        self.fields["feedback"] = forms.CharField(
            label=_("Your feedback"),
            widget=forms.Textarea(
                attrs={"placeholder": _("Please let us know if anything is missing")}
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
            question_answers = SurveyQuestionAnswer.objects.filter(
                pk__in=answers
            ).order_by("aindex")
            for question_answer in question_answers:
                # Validate if answer is unique.
                if question_answer.uniqueAnswer:
                    answer_text = _(question_answer[0].label)

                    raise forms.ValidationError(
                        _(
                            "You can't choose multiple answers if the answer {} is choosen.".format(
                                answer_text
                            )
                        )
                    )

                # Validate answers' dependencies.
                dependant_answers = question_answer.dependant_answers.all()
                for dependant_answer in dependant_answers:
                    if str(dependant_answer.id) in answers:
                        dependant_answers_str = [
                            str(dep_answer) for dep_answer in dependant_answers
                        ]
                        raise forms.ValidationError(
                            _(
                                "You can't choose the answers {} if answer '{}' is choosen.".format(
                                    dependant_answers_str,
                                    question_answer,
                                )
                            )
                        )

        return answers

    def set_answer_content(self, answer_content):
        self.fields["answer_content"].initial = answer_content

    def set_feedback(self, feedback):
        self.fields["feedback"].initial = feedback


class GeneralFeedback(forms.Form):
    def __init__(self, *args, **kwargs):
        kwargs.pop("lang")

        super().__init__(*args, **kwargs)

        self.fields["general_feedback"] = forms.CharField(
            label=_("Your feedback"),
            widget=forms.Textarea(
                attrs={"placeholder": _("Please let us know if anything is missing")}
            ),
            required=True,
        )

    def set_general_feedback(self, feedback):
        self.fields["general_feedback"].initial = feedback
