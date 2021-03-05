import datetime

from bootstrap_modal_forms.forms import BSModalModelForm
from django import forms

from .models import Company, Technology, Industry


def current_year():
    return int(datetime.date.today().year)


class CompanyForm(BSModalModelForm):

    CHOICES = ((year, year) for year in range(current_year() - 40, current_year() + 1))
    established_year = forms.ChoiceField(choices=CHOICES, required=False)
    description = forms.CharField(widget=forms.Textarea(attrs={"rows": 4, "style": "resize: none;"}), required=False)

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



class TechnologyForm(BSModalModelForm):
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


class IndustryForm(BSModalModelForm):

    def __init__(self, *args, **kwargs):
        super(IndustryForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                "class": "form-control",
                "id": "industry-input"
            })

    name = forms.CharField(label='Industry', max_length=50, widget=forms.TextInput())

    class Meta:
        model = Industry
        fields = {
            'name'
        }
