from allauth.account.models import EmailAddress
from django.contrib.auth.models import User


def is_social(request):
    try:
        user = User.objects.get(username=request.user)
    except User.DoesNotExist:
        user = None
    try:
        email = EmailAddress.objects.get(user=user)
    except EmailAddress.DoesNotExist:
        email = None
    if email:
        return {"profile_is_social": True}
    else:
        return {"profile_is_social": False}
