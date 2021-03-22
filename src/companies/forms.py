import datetime

from bootstrap_modal_forms.forms import BSModalModelForm
from django import forms
from django.contrib.auth.models import User

from .models import Company, Technology, Industry


def current_year():
    return int(datetime.date.today().year)


class CompanyForm(BSModalModelForm):

    def __init__(self, *args, **kwargs):
        super(CompanyForm, self).__init__(*args, **kwargs)
        self.initial = {"user": self.request.user}
        self.fields['user'] = forms.ModelChoiceField(queryset=User.objects.all().filter(username=self.request.user),
                                                     label='User',
                                                     widget=forms.HiddenInput(),
                                                     empty_label=None)
        self.fields['technologies'] = forms.ModelMultipleChoiceField(
            widget=forms.CheckboxSelectMultiple(attrs={"class": "list-unstyled row"}),
            queryset=Technology.objects.all().filter(
                user=self.request.user
            ),
        )
        self.fields['industry'] = forms.ModelChoiceField(
            queryset=Industry.objects.filter(user=self.request.user),
            empty_label=None
        )
        self.fields['company_size'].choices = self.fields['company_size'].choices[1:]

    CHOICES = ((year, year) for year in range(current_year() - 20, current_year() + 1))
    established_year = forms.ChoiceField(choices=CHOICES, required=False)
    description = forms.CharField(widget=forms.Textarea(attrs={"rows": 4, "style": "resize: none;"}), required=False)

    class Meta:
        model = Company
        fields = (
            'name',
            'user',
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
                "id": f"{name}-input"
            })
        self.initial = {"user": self.request.user}
        self.fields['user'] = forms.ModelChoiceField(queryset=User.objects.all().filter(username=self.request.user),
                                                     label='User',
                                                     widget=forms.HiddenInput(),
                                                     empty_label=None)

    name = forms.CharField(label='Technology', max_length=50, widget=forms.TextInput(), required=True)

    class Meta:
        model = Technology
        fields = {
            'name',
            'user'
        }

    # case insensitive check of existing objects for current user
    def clean(self):
        cleaned_data = super(TechnologyForm, self).clean()
        name = cleaned_data.get('name')
        if name and Technology.objects.filter(user=self.request.user, name__iexact=name).exists():
            self.add_error('name', 'Technology with this name is already exists.')
        return cleaned_data


class IndustryForm(BSModalModelForm):

    def __init__(self, *args, **kwargs):
        super(IndustryForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                "class": "form-control",
                "id": f"{name}-input"
            })
        self.initial = {"user": self.request.user}
        self.fields['user'] = forms.ModelChoiceField(queryset=User.objects.all().filter(username=self.request.user),
                                                     label='User',
                                                     widget=forms.HiddenInput(),
                                                     empty_label=None)

    name = forms.CharField(label='Industry', max_length=50, widget=forms.TextInput())

    # case insensitive check of existing objects for current user
    def clean(self):
        cleaned_data = super(IndustryForm, self).clean()
        name = cleaned_data.get('name')
        if name and Industry.objects.filter(name__iexact=name, user=self.request.user).exists():
            self.add_error('name', 'Industry with this name is already exists.')
        return cleaned_data

    class Meta:
        model = Industry
        fields = {
            'name',
            'user'
        }
