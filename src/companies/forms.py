import datetime
from django import forms

from .models import Company, Technology


def current_year():
    return int(datetime.date.today().year)


class CompanyForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CompanyForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                "class": "form-control"
            })

    CHOICES = ((year, year) for year in range(current_year() - 21, current_year() + 1))
    name = forms.CharField(
        label="Company name",
        max_length=100,
        widget=forms.TextInput(
        ),
        required=True
    )
    industry = forms.CharField(
        label='Industry',
        max_length=100,
        widget=forms.Select(
        )
    )
    established_year = forms.ChoiceField(choices=CHOICES)

    class Meta:
        model = Company
        fields = (
            'name',
            'industry',
            'technologies',
            'established_year',
            'description',
            'company_size',
            'location',
            'url'
        )


class TechnologyForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(TechnologyForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                "class": "form-control",
                "id": "techno-input"
            })

    name = forms.CharField(label='Technology', max_length=50, widget=forms.TextInput())

    class Meta:
        model = Technology
        fields = {
            'name'
        }