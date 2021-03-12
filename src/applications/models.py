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

    date = models.DateField()
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    position = models.CharField(max_length=200)
    portal = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.APPLIED)

    @classmethod
    def get_statuses(cls):
        return [status.label for status in cls.Status]


class Resume(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=200)
    file = models.FileField(upload_to='resume')
