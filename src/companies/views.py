from bootstrap_modal_forms.generic import BSModalCreateView, BSModalDeleteView, BSModalReadView, BSModalUpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render
from django.utils.decorators import method_decorator

from companies.models import Company, Technology, Industry

from companies.forms import CompanyForm, TechnologyForm, IndustryForm
from django.urls import reverse_lazy


@login_required
def company_list(request):
    username = request.user
    companies = Company.objects.all().filter(user=username)
    technologies = Technology.objects.all().filter(user=username)
    industries = Industry.objects.all().filter(user=username)
    return render(
        request,
        'companies/list.html',
        context={
            "companies": companies,
            "technologies": technologies,
            "industries": industries,
        }
    )


@method_decorator(login_required, name='dispatch')
class TechnologyCreateView(BSModalCreateView, LoginRequiredMixin):
    template_name = 'companies/content/technology_create.html'
    form_class = TechnologyForm
    success_message = 'Success: created!'
    success_url = reverse_lazy('companies_list')


@method_decorator(login_required, name='dispatch')
class TechnologyUpdateView(BSModalUpdateView, LoginRequiredMixin):
    model = Technology
    template_name = 'companies/content/technology_update.html'
    form_class = TechnologyForm
    success_message = 'Success: updated!'
    success_url = reverse_lazy('companies_list')


@method_decorator(login_required, name='dispatch')
class TechnologyDeleteView(BSModalDeleteView, LoginRequiredMixin):
    model = Technology
    template_name = 'companies/content/technology_delete.html'
    success_message = 'Success: deleted!'
    success_url = reverse_lazy('companies_list')


@method_decorator(login_required, name='dispatch')
class IndustryCreateView(BSModalCreateView, LoginRequiredMixin):
    template_name = 'companies/content/industry_create.html'
    form_class = IndustryForm
    success_message = 'Success: created!'
    success_url = reverse_lazy('companies_list')


@method_decorator(login_required, name='dispatch')
class IndustryUpdateView(BSModalUpdateView, LoginRequiredMixin):
    model = Industry
    template_name = 'companies/content/industry_update.html'
    form_class = IndustryForm
    success_message = 'Success: updated!'
    success_url = reverse_lazy('companies_list')


@method_decorator(login_required, name='dispatch')
class IndustryDeleteView(BSModalDeleteView, LoginRequiredMixin):
    model = Industry
    template_name = 'companies/content/industry_delete.html'
    success_message = 'Success: deleted!'
    success_url = reverse_lazy('companies_list')


@method_decorator(login_required, name='dispatch')
class CompanyCreateView(BSModalCreateView, LoginRequiredMixin):
    model = Company
    template_name = 'companies/company_create.html'
    form_class = CompanyForm
    success_message = 'Success: created!'
    success_url = reverse_lazy('companies_list')


@method_decorator(login_required, name='dispatch')
class CompanyUpdateView(BSModalUpdateView, LoginRequiredMixin):
    model = Company
    template_name = 'companies/company_update.html'
    form_class = CompanyForm
    success_message = 'Success: updated!'
    success_url = reverse_lazy('companies_list')

    def get_context_data(self, **kwargs):
        instance = super().get_context_data(**kwargs)
        instance['technologies'] = [str(technology) for technology in instance['object'].technologies.all()]
        return instance


@method_decorator(login_required, name='dispatch')
class CompanyDeleteView(BSModalDeleteView, LoginRequiredMixin):
    model = Company
    template_name = 'companies/company_delete.html'
    success_message = 'Success: deleted!'
    success_url = reverse_lazy('companies_list')


@method_decorator(login_required, name='dispatch')
class CompanyReadView(BSModalReadView, LoginRequiredMixin):
    model = Company
    template_name = 'companies/company_read.html'
