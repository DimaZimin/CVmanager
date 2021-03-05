from bootstrap_modal_forms.generic import BSModalCreateView, BSModalDeleteView, BSModalReadView, BSModalUpdateView
from django.shortcuts import render
from companies.models import Company, Technology, Industry

from companies.forms import CompanyForm, TechnologyForm, IndustryForm
from django.urls import reverse_lazy


def company_list(request):
    companies = Company.objects.all()
    return render(request, 'companies/list.html', context={"companies": companies})


def content_manager(request):
    technologies = Technology.objects.all()
    industries = Industry.objects.all()
    return render(
        request,
        'companies/content_manager.html',
        context=
        {
            "technologies": technologies,
            "industries": industries,
        }
    )


class TechnologyCreateView(BSModalCreateView):
    template_name = 'companies/content/technology_create.html'
    form_class = TechnologyForm
    success_message = 'Success: created!'
    success_url = reverse_lazy('content_manager')


class TechnologyUpdateView(BSModalUpdateView):
    model = Technology
    template_name = 'companies/content/technology_update.html'
    form_class = TechnologyForm
    success_message = 'Success: updated!'
    success_url = reverse_lazy('content_manager')


class TechnologyDeleteView(BSModalDeleteView):
    model = Industry
    template_name = 'companies/content/technology_delete.html'
    success_message = 'Success: deleted!'
    success_url = reverse_lazy('content_manager')


class IndustryCreateView(BSModalCreateView):
    template_name = 'companies/content/industry_create.html'
    form_class = IndustryForm
    success_message = 'Success: created!'
    success_url = reverse_lazy('content_manager')


class IndustryUpdateView(BSModalUpdateView):
    model = Industry
    template_name = 'companies/content/industry_update.html'
    form_class = IndustryForm
    success_message = 'Success: updated!'
    success_url = reverse_lazy('content_manager')


class IndustryDeleteView(BSModalDeleteView):
    model = Industry
    template_name = 'companies/content/industry_delete.html'
    success_message = 'Success: deleted!'
    success_url = reverse_lazy('content_manager')


class CompanyCreateView(BSModalCreateView):
    model = Company
    template_name = 'companies/company_create.html'
    form_class = CompanyForm
    success_message = 'Success: created!'
    success_url = reverse_lazy('companies_list')


class CompanyUpdateView(BSModalUpdateView):
    model = Company
    template_name = 'companies/company_update.html'
    form_class = CompanyForm
    success_message = 'Success: updated!'
    success_url = reverse_lazy('companies_list')


class CompanyDeleteView(BSModalDeleteView):
    model = Company
    template_name = 'companies/company_delete.html'
    success_message = 'Success: deleted!'
    success_url = reverse_lazy('companies_list')


class CompanyReadView(BSModalReadView):
    model = Company
    template_name = 'companies/company_read.html'
