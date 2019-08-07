from django import forms

from survey.globals import SECTOR_CHOICES, COMPANY_SIZE


class InitialStartForm(forms.Form):
    userid = forms.CharField(widget=forms.HiddenInput())
    sector = forms.ChoiceField(widget=forms.Select, choices=SECTOR_CHOICES)
    compSize = forms.ChoiceField(widget=forms.Select, choices=COMPANY_SIZE)


    def setQuestions(self, q1, q2):
        self.fields['sector'].label = q1
        self.fields['compSize'].label = q2

    def setUID(self,uid):
        self.fields['userid'].initial = uid

class AnswerMChoice(forms.Form):
    userid = forms.CharField(widget=forms.HiddenInput())
    answers = forms.MultipleChoiceField(choices=[], widget=forms.CheckboxSelectMultiple())
    
    def __init__(self, answers=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if answers != None:
            self.fields['answers'].choices = answers

    def setUID(self,uid):
        self.fields['userid'].initial = uid
