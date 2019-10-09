from django import forms

from survey.globals import SECTOR_CHOICES, COMPANY_SIZE, TRANSLATION_UI
from survey.models import SurveyQuestionAnswer, TranslationKey


class InitialStartForm(forms.Form):
    userid = forms.CharField(widget=forms.HiddenInput())
    sector = forms.ChoiceField(
        required=True, widget=forms.Select, choices=SECTOR_CHOICES)
    compSize = forms.ChoiceField(
        required=True, widget=forms.Select, choices=COMPANY_SIZE)

    def __init__(self, translations=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if translations != None:
            self.fields['sector'].label = translations['sector']
            self.fields['compSize'].label = translations['compSize']
        else:
            self.fields['sector'].label = "What is your sector?"
            self.fields['compSize'].label = "How many employees?"

    def setUID(self, uid):
        self.fields['userid'].initial = uid


class AnswerMChoice(forms.Form):
    userid = forms.CharField(widget=forms.HiddenInput())
    questionid = forms.IntegerField(widget=forms.HiddenInput())

    answers = forms.MultipleChoiceField(required=True, choices=[], widget=forms.CheckboxSelectMultiple(), label='')

    def __init__(self, tanswers=None, *args, **kwargs):
        self.lang = kwargs.pop('lang')

        super().__init__(*args, **kwargs)

        self.fields['answers'].error_messages = {
            'required': TRANSLATION_UI["form"]["error_messages"]["answer"]["required"][self.lang.lower()]
        }

        if tanswers != None:
            self.fields['answers'].choices = tanswers

    def setUID(self, uid):
        self.fields['userid'].initial = uid

    def set_question_id(self, question_id):
        self.fields['questionid'].initial = question_id

    def clean_answers(self):
        answers = self.cleaned_data['answers']

        if len(answers) > 1:
            unique_answer = SurveyQuestionAnswer.objects.filter(pk__in=answers, uniqueAnswer=1)
            if unique_answer.count():
                translation_key = TranslationKey.objects.filter(lang=self.lang, key=unique_answer[0].answerKey)
                answer_text = translation_key[0].text

                raise forms.ValidationError(
    TRANSLATION_UI["form"]["error_messages"]["answer"]["unique"][self.lang.lower()], params={'value': answer_text})

        return answers
