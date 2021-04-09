from django.shortcuts import render


def error_404(request, exception):
    return render(request, '404.html')


def error_500(request):
    return render(request, '500.html')


def index(request):
    user = request.user
    if user.is_anonymous:
        user = None
    return render(request, 'index.html', {"user": user})
