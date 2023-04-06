from datetime import datetime

from bootstrap_datepicker_plus.widgets import DatePickerInput
from django import forms


class DatesLimitForm(forms.Form):
    start_date = forms.DateField(widget=DatePickerInput())
    end_date = forms.DateField(
        widget=DatePickerInput(
            options={"maxDate": datetime.now().strftime("%Y-%m-%d")},
            range_from="start_date",
        )
    )

    def __init__(self, *args, **kwargs):
        initial_start_date = kwargs.pop("start_date", None)
        initial_end_date = kwargs.pop("end_date", None)
        minDate_start_date = kwargs.pop("minDate", None)

        super().__init__(*args, **kwargs)
        self.fields["start_date"].initial = initial_start_date
        self.fields["start_date"].widget.config.options = {
            "minDate": minDate_start_date
        }
        self.fields["end_date"].initial = initial_end_date
