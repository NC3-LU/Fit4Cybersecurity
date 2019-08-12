from django import forms

from survey.globals import SECTOR_CHOICES, COMPANY_SIZE


class InitialStartForm(forms.Form):
    userid = forms.CharField(widget=forms.HiddenInput())
    sector = forms.ChoiceField(widget=forms.Select, choices=SECTOR_CHOICES)
    compSize = forms.ChoiceField(widget=forms.Select, choices=COMPANY_SIZE)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
        self.fields['sector'].label = "What is your sector?"
        self.fields['compSize'].label = "How many employees?"

    def setUID(self,uid):
        self.fields['userid'].initial = uid

class AnswerMChoice(forms.Form):
    userid = forms.CharField(widget=forms.HiddenInput())
    answers = forms.MultipleChoiceField(choices=[], widget=forms.CheckboxSelectMultiple(), label='')
    
    def __init__(self, answers=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if answers != None:
            self.fields['answers'].choices = answers

    def setUID(self,uid):
        self.fields['userid'].initial = uid
