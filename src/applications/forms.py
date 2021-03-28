import datetime

from bootstrap_modal_forms.forms import BSModalModelForm
from django import forms
from django.contrib.auth.models import User

from applications.models import Application
from companies.models import Company


def max_date_today():
    return str(datetime.datetime.today().date())


class ApplicationForm(BSModalModelForm):

    def __init__(self, *args, **kwargs):
        super(ApplicationForm, self).__init__(*args, **kwargs)
        self.initial = {"user": self.request.user}
        self.fields['user'] = forms.ModelChoiceField(
            queryset=User.objects.filter(username=self.request.user),
            label='User',
            widget=forms.HiddenInput(),
            empty_label=None)
        self.fields['company'] = forms.ModelChoiceField(
            queryset=Company.objects.filter(user=self.request.user),
            label='Company',
            empty_label=None,
            widget=forms.Select()
        )

    date = forms.DateField(
        label='Date',
        widget=forms.DateInput(
            attrs={
                "max": max_date_today(),
                "min": "2020-01-01",
                "type": "date",
            }
        )
    )

    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "rows": 4,
                "style": "resize: none;"
            }
        ),
        required=False
    )

    class Meta:
        model = Application
        fields = {
            "user",
            "date",
            "company",
            "position",
            "portal",
            "status",
            "description"
        }