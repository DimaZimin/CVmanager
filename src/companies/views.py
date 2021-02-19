from django.shortcuts import render

# Create your views here.
from companies.models import Company

from companies.forms import CompanyForm


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
