from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalDeleteView, BSModalReadView, BSModalUpdateView
from django.urls import reverse_lazy

from applications.forms import ApplicationForm
from applications.models import Application


@login_required
def application_list(request):
    applications = Application.objects.all().filter(user=request.user)
    return render(request, 'applications/list.html', {"applications": applications})


class ApplicationCreateView(BSModalCreateView):
    model = Application
    template_name = 'applications/application_create.html'
    form_class = ApplicationForm
    success_message = 'Success! Application has been registered.'
    success_url = reverse_lazy('applications_list')


class ApplicationUpdateView(BSModalUpdateView):
    model = Application
    template_name = 'applications/application_update.html'
    form_class = ApplicationForm
    success_message = 'Success! Application has been updated.'
    success_url = reverse_lazy('applications_list')


class ApplicationDeleteView(BSModalDeleteView):
    model = Application
    template_name = 'applications/application_delete.html'
    success_message = 'Success! Application has been deleted.'
    success_url = reverse_lazy('applications_list')


class ApplicationReadView(BSModalReadView):
    model = Application
    template_name = 'applications/application_read.html'
