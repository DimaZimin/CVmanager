from django import forms

from companies.models import Company


class CompanyForm(forms.ModelForm):
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
