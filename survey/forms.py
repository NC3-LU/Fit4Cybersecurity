from django import forms

from survey.globals import SECTOR_CHOICES, COMPANY_SIZE, TRANSLATION_UI
from survey.models import SurveyQuestionAnswer, TranslationKey
from django_countries.fields import CountryField

class InitialStartForm(forms.Form):
    sector = forms.ChoiceField(required=True, widget=forms.Select)
    compSize = forms.ChoiceField(required=True, widget=forms.Select, choices=COMPANY_SIZE)

    def __init__(self, translations=None, *args, **kwargs):
        lang = kwargs.pop('lang')

        super().__init__(*args, **kwargs)

        self.fields['sector'].label = TRANSLATION_UI["form"]["start_form"]["sector_question"][lang]
        sectors = []
        for sector_choise in SECTOR_CHOICES:
            sectors.append((sector_choise[0], TRANSLATION_UI["form"]
               ["start_form"]["sector_list"][sector_choise[0]][lang]))

        self.fields['sector'].choices = sectors
        self.fields['compSize'].label = TRANSLATION_UI["form"]["start_form"]["size_question"][lang]

        country_label = TRANSLATION_UI["form"]["start_form"]["country"]["label"][lang]
        required_error_message = TRANSLATION_UI["form"]["start_form"]["country"]["required_error_message"][lang.lower()]
        self.fields['country'] = CountryField().formfield(label=country_label, required=True, initial="LU",
            error_messages = {'required': required_error_message})


class AnswerMChoice(forms.Form):
    unique_answers = forms.CharField(widget=forms.HiddenInput(), required=False)

    def __init__(self, tanswers=None, *args, **kwargs):
        self.lang = kwargs.pop('lang')
        answers_field_type = kwargs.pop('answers_field_type')

        super().__init__(*args, **kwargs)

        if answers_field_type == 'M':
            self.fields['answers'] = forms.MultipleChoiceField(
                required=True,
                choices=[],
                widget=forms.CheckboxSelectMultiple(attrs={'class': 'multiple-selection'}),
                label='')
        elif answers_field_type == 'S':
            self.fields['answers'] = forms.ChoiceField(
                required=True,
                choices=[],
                widget=forms.RadioSelect(attrs={'class': 'radio-buttons'}),
                label='')

        self.fields['answers'].error_messages = {
            'required': TRANSLATION_UI["form"]["error_messages"]["answer"]["required"][self.lang]
        }

        if tanswers != None:
            self.fields['answers'].choices = tanswers

        self.fields['feedback'] = forms.CharField(label=TRANSLATION_UI['form']['questions']['feedback_label'][self.lang],
            widget=forms.Textarea(attrs={'placeholder': TRANSLATION_UI['form']['questions']['feedback_placeholder'][self.lang]}),
            required=False)

    def set_unique_answers(self, unique_answers_ids):
        self.fields['unique_answers'].initial = unique_answers_ids

    def set_answers(self, answers_ids):
        self.fields['answers'].initial = answers_ids

    def clean_answers(self):
        answers = self.cleaned_data['answers']
        if self.fields['answers'].widget.input_type == 'radio':
            answers = [answers]

        if len(answers) > 1:
            unique_answer = SurveyQuestionAnswer.objects.filter(
                pk__in=answers, uniqueAnswer=1)
            if unique_answer.count():
                translation_key = TranslationKey.objects.filter(
                    lang=self.lang, key=unique_answer[0].answerKey)
                answer_text = translation_key[0].text

                raise forms.ValidationError(
                    TRANSLATION_UI["form"]["error_messages"]["answer"]["unique"][self.lang],
                    params={'value': answer_text})

        return answers

    def set_feedback(self, feedback):
        self.fields['feedback'].initial = feedback
