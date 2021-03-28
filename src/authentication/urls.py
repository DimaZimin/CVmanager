from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^login/$', views.login_page, name='authentication_login'),
    url(r'^register/$', views.register_page, name='authentication_register'),
    url(r'^logout/$', views.logout_page, name='authentication_logout'),
    path('activate/<uidb64>/<token>', views.activate, name='authentication_activate'),
    url(r'^password/$', views.change_password, name='authentication_change_password'),
    url(r'^delete_profile/$', views.delete_account, name='authentication_delete_profile'),
    url(r'^pasword_reset/$', auth_views.PasswordResetView.as_view(
        template_name="authentication/password_reset/reset_form.html"),
        name='password_reset'),
    url(r'^password_reset/done/$', auth_views.PasswordResetDoneView.as_view(
        template_name="authentication/password_reset/done.html"
    ),
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,40})/$',
        auth_views.PasswordResetConfirmView.as_view(
            template_name="authentication/password_reset/confirm.html"
        ),
        name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.PasswordResetCompleteView.as_view(
        template_name="authentication/password_reset/complete.html"
    ),
        name='password_reset_complete')
]
