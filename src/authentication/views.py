from allauth.account.models import EmailAddress
from allauth.exceptions import ImmediateHttpResponse
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.socialaccount.models import SocialAccount
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from authentication.form import UserRegistrationForm
from authentication.tokens import account_activation_token


class MyAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        email = sociallogin.email_addresses[0]
        if sociallogin.is_existing:
            return ImmediateHttpResponse(redirect('dashboard'))
        try:
            user = User.objects.get(email=email)
            sociallogin.connect(request, user)
        except User.DoesNotExist:
            return ImmediateHttpResponse(redirect('authentication_login'))
        try:
            email_address = EmailAddress.objects.get(email__iexact=str(email))
            user = email_address.user
            sociallogin.connect(request, user)
        except EmailAddress.DoesNotExist:
            return ImmediateHttpResponse(redirect('authentication_login'))


def login_page(request):
    error = False
    if request.method == 'POST':
        user = authenticate(
            username=request.POST.get('login'),
            password=request.POST.get('password')
        )
        if user and user.is_active:
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
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your account'
            message = render_to_string('authentication/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                subject=mail_subject, body=message, to=[to_email]
            )
            email.content_subtype = 'html'
            email.send()
            return render(request, 'authentication/activate_registration.html', {
                'email': to_email,
                'user': user
            })

    return render(
        request,
        'authentication/register.html',
        {
            "form": form
        }
    )


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        messages.success(request, 'Your account has been activated.')
        return redirect('dashboard')
    else:
        return HttpResponse('Activation link is invalid')


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'authentication/change_password.html', {
        "form": form
    })


def delete_account(request):
    if request.method == 'POST':
        username = request.user
        user = User.objects.get(username=username)
        user.delete()
        try:
            user_account = EmailAddress.objects.get(email=user.email)
            user_account.delete()
        except EmailAddress.DoesNotExist:
            pass
        try:
            user_social = SocialAccount.objects.get(user=user)
            user_social.delete()
        except SocialAccount.DoesNotExist:
            pass
        logout(request)
        messages.success(request, 'Your account has been deleted.')
        return redirect('authentication_login')
    else:
        return render(request, 'authentication/delete_profile.html')


def logout_page(request):
    logout(request)
    return redirect('authentication_login')