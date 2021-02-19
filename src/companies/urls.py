from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^list/$', views.company_list, name='companies_list')
]
