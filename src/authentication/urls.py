from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'login/$', views.login_page, name='authentication_login'),
    url(r'register/$', views.register_page, name='authentication_register'),
    url(r'logout/$', views.logout_page, name='authentication_logout')
]