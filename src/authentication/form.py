from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(
        max_length=200,
        label='Username',
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "username"
            }
        ),
        required=True
    )
    email = forms.EmailField(
        max_length=200,
        label='E-mail',
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "e-mail"
            }
        ),
        required=True
    )
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "password"
            }
        ),
        required=True
    )
    password2 = forms.CharField(
        label="Repeat password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "password"
            }
        ),
        required=True
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            match = User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('This email is already in use.')