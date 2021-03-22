from django.contrib.auth import authenticate, logout, login
from django.shortcuts import render, redirect

from authentication.form import UserRegistrationForm


def login_page(request):
    error = False
    if request.method == 'POST':
        user = authenticate(
            username=request.POST.get('login'),
            password=request.POST.get('password')
        )
        if user:
            login(request, user)
            return redirect(
                'dashboard'
            )
        else:
            error = True
    return render(
        request,
        'authentication/login.html',
        {
            "error": error
        }
    )


def register_page(request):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password1')
            )
            if user:
                login(request, user)
            return redirect('dashboard')
    return render(
        request,
        'authentication/register.html',
        {
            "form": form
        }
    )


def logout_page(request):
    logout(request)
    return redirect('authentication_login')