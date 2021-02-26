from django.contrib import messages
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from companies.models import Company, Technology

from companies.forms import CompanyForm, TechnologyForm


def company_list(request):
    companies = Company.objects.all()
    return render(
        request,
        'companies/list.html',
        context=
        {
            "companies": companies
        }
    )


def company_add(request):
    form = CompanyForm(request.POST or None)
    return render(request,
                  'companies/add.html',
                  context={"form": form})


def content_manager(request):
    pass


def add_technology(request):
    if request.is_ajax() and request.method == "POST":
        form = TechnologyForm(request.POST)
        if form.is_valid():
            instance = form.save()
            serialized_instance = serializers.serialize('json', [instance, ])
            messages.add_message(request, messages.INFO, "Success")
            return JsonResponse({"instance": serialized_instance}, status=200)
        else:
            return JsonResponse({"error": form.errors}, status=400)
    if request.method == "GET":
        form = TechnologyForm()
        return render(request, "companies/add_technology.html", context={"form": form
        })
    return JsonResponse({"error": ""}, status=400)
