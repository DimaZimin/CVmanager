import datetime

from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


class Company(models.Model):
    CHOICES = [
        ('<10', '<10'),
        ('10-20', '10-20'),
        ('20-50', '20-50'),
        ('50-100', '50-100'),
        ('100+', '100+'),
        ('250+', '250+'),
        ('500+', '500+')
    ]

    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    industry = models.ForeignKey('Industry', on_delete=models.CASCADE, null=True, blank=True)
    technologies = models.ManyToManyField('Technology', blank=True)
    established_year = models.IntegerField(validators=[MinValueValidator(1980), max_value_current_year], null=True,
                                           blank=True)
    description = models.TextField(null=True, blank=True)
    company_size = models.CharField(max_length=10, choices=CHOICES, null=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    url = models.URLField(default="", null=True, blank=True)

    def __str__(self):
        return self.name


class Technology(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('name', 'user')

    def __str__(self):
        return self.name


class Industry(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('name', 'user')

    def __str__(self):
        return self.name
