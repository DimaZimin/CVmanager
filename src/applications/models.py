from django.db import models
from django.utils.translation import gettext_lazy as _
from companies.models import Company


class Application(models.Model):
    class Status(models.TextChoices):
        APPLIED = 'APPLIED', _('Applied')
        RESPOND = 'RESPOND', _('Respond received'),
        REJECTED = 'REJECTED', _('Rejected'),
        INVITED = 'INVITED', _('Interview invitation received'),
        PASSED = 'PASSED', _('Interview passed'),
        FAILED = 'FAILED', _('Interview failed'),
        OFFERED = 'OFFERED', _('Job offer received')

    date = models.DateField()
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    position = models.ForeignKey('Position', on_delete=models.PROTECT)
    portal = models.ForeignKey('JobPortal', on_delete=models.PROTECT)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.APPLIED)


class JobPortal(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()


class Position(models.Model):
    name = models.CharField(max_length=255)


class Resume(models.Model):
    name = models.CharField(max_length=255)
    position = models.ForeignKey(Position, on_delete=models.PROTECT)
    file = models.FileField(upload_to='resume')
