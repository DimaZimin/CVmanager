from bootstrap_modal_forms.forms import BSModalModelForm
from django import forms

from applications.models import Application


class ApplicationForm(BSModalModelForm):

    date = forms.DateField(
        label='Date',
        widget=forms.DateInput(
            attrs={
                "max": "2029-12-31",
                "min": "2020-01-01",
                "type": "date",
            }
        )
    )

    class Meta:
        model = Application
        fields = {
            "date",
            "company",
            "position",
            "portal",
            "status"
        }