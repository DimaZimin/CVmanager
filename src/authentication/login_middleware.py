from django.shortcuts import redirect
from django.conf import settings


def login_required_middleware(get_response):
    def middleware(request):
        if not request.user.is_authenticated and request.path not in settings.LOGIN_EXEMPT_URLS:
            return redirect(settings.LOGIN_URL)
        response = get_response(request)
        return response
    return middleware
