from django import forms

from survey.globals import SECTOR_CHOICES, COMPANY_SIZE, TRANSLATION_UI
from survey.models import SurveyQuestionAnswer, TranslationKey


class InitialStartForm(forms.Form):
    userid = forms.CharField(widget=forms.HiddenInput())
    sector = forms.ChoiceField(required=True, widget=forms.Select)
    compSize = forms.ChoiceField(required=True, widget=forms.Select, choices=COMPANY_SIZE)

    def __init__(self, translations=None, *args, **kwargs):
        lang = kwargs.pop('lang')

        super().__init__(*args, **kwargs)

        self.fields['sector'].label = TRANSLATION_UI["form"]["start_form"]["sector_question"][lang.lower()]
        sectors = []
        for sector_choise in SECTOR_CHOICES:
            sectors.append((sector_choise[0], TRANSLATION_UI["form"]
               ["start_form"]["sector_list"][sector_choise[0]][lang.lower()]))

        self.fields['sector'].choices = sectors
        self.fields['compSize'].label = TRANSLATION_UI["form"]["start_form"]["size_question"][lang.lower()]

    def setUID(self, uid):
        self.fields['userid'].initial = uid


class AnswerMChoice(forms.Form):
    userid = forms.CharField(widget=forms.HiddenInput())
    questionid = forms.IntegerField(widget=forms.HiddenInput())

    def __init__(self, tanswers=None, *args, **kwargs):
        self.lang = kwargs.pop('lang')
        answers_field_type = kwargs.pop('answers_field_type')

        super().__init__(*args, **kwargs)

        if answers_field_type == 'M':
            self.fields['answers'] = forms.MultipleChoiceField(required=True, choices=[], widget=forms.CheckboxSelectMultiple, label='')
        elif answers_field_type == 'S':
            self.fields['answers'] = forms.ChoiceField(required=True, choices=[], widget=forms.RadioSelect, label='')

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
        if self.fields['answers'].widget.input_type == 'radio':
            answers = [answers]

        if len(answers) > 1:
            unique_answer = SurveyQuestionAnswer.objects.filter(pk__in=answers, uniqueAnswer=1)
            if unique_answer.count():
                translation_key = TranslationKey.objects.filter(lang=self.lang, key=unique_answer[0].answerKey)
                answer_text = translation_key[0].text

                raise forms.ValidationError(TRANSLATION_UI["form"]["error_messages"]
                            ["answer"]["unique"][self.lang.lower()], params={'value': answer_text})


        return answers
