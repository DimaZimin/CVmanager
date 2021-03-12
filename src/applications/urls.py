from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^list/$', views.application_list, name='applications_list'),
    url(r'^create/$', views.ApplicationCreateView.as_view(), name='applications_create'),
    url(r'^update/(?P<pk>\d+)/$', views.ApplicationUpdateView.as_view(), name='applications_update'),
    url(r'^delete/(?P<pk>\d+)/$', views.ApplicationDeleteView.as_view(), name='applications_delete'),
    url(r'^read/(?P<pk>\d+)/$', views.ApplicationReadView.as_view(), name='applications_read'),
]
