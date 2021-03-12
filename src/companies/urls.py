from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^list/$', views.company_list, name='companies_list'),
    url(r'^technologies/create/$', views.TechnologyCreateView.as_view(), name='technology_create'),
    url(r'^technologies/(?P<pk>\d+)/update/$', views.TechnologyUpdateView.as_view(), name='technology_update'),
    url(r'^technologies/(?P<pk>\d+)/delete/$', views.TechnologyDeleteView.as_view(), name='technology_delete'),
    url(r'^industries/create/$', views.IndustryCreateView.as_view(), name='industry_create'),
    url(r'^industries/(?P<pk>\d+)/update/$', views.IndustryUpdateView.as_view(), name='industry_update'),
    url(r'^industries/(?P<pk>\d+)/delete/$', views.IndustryDeleteView.as_view(), name='industry_delete'),
    url(r'^create/$', views.CompanyCreateView.as_view(), name='company_create'),
    url(r'^(?P<pk>\d+)/read/$', views.CompanyReadView.as_view(), name='company_read'),
    url(r'^(?P<pk>\d+)/update/$', views.CompanyUpdateView.as_view(), name='company_update'),
    url(r'^(?P<pk>\d+)/delete/$', views.CompanyDeleteView.as_view(), name='company_delete'),
]
