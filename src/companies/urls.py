from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^list/$', views.company_list, name='companies_list'),
    url(r'^add/$', views.company_add, name='companies_add'),
    url(r'^technologies/add/$', views.add_technology, name='companies_add_technology'),
]
