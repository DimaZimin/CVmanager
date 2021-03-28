from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _
from companies.models import Company


class Application(models.Model):
    class Status(models.TextChoices):
        APPLIED = 'APPLIED', _('No respond')
        RESPOND = 'RESPOND', _('Respond received'),
        REJECTED = 'REJECTED', _('Rejected'),
        INVITED = 'INVITED', _('Interview invitation received'),
        PASSED = 'PASSED', _('Interview passed'),
        FAILED = 'FAILED', _('Interview failed'),
        OFFERED = 'OFFERED', _('Job offer received')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    position = models.CharField(max_length=200, null=True, blank=True)
    portal = models.CharField(max_length=200, null=True, blank=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.APPLIED)
    description = models.TextField(max_length=2000, null=True, blank=True)

    @classmethod
    def get_statuses(cls):
        return [status.label for status in cls.Status]


class Resume(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=200)
    file = models.FileField(upload_to='resume')
