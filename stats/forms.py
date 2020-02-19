from bootstrap_datepicker_plus import DatePickerInput
from django import forms
from datetime import datetime, timedelta

DEFAULT_DATE_FORMAT = "%Y-%m-%d"

def one_month_before_today():
    return datetime.now() - timedelta(days=30)

class DatesLimitForm(forms.Form):
    start_date = forms.DateField(
        widget=DatePickerInput(format=DEFAULT_DATE_FORMAT).start_of('event'),
        initial=one_month_before_today()
    )
    end_date = forms.DateField(
        widget=DatePickerInput(format=DEFAULT_DATE_FORMAT).end_of('event'),
        initial=datetime.today()
    )
