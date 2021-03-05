import datetime

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from smart_selects.db_fields import ChainedForeignKey


def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


# class Country(models.Model):
#     name = models.CharField(max_length=255)
#
#
# class City(models.Model):
#     country = models.ForeignKey(Country, on_delete=models.CASCADE)
#     name = models.CharField(max_length=255)
#
#
# class Location(models.Model):
#     country = models.ForeignKey(Country, on_delete=models.CASCADE)
#     city = ChainedForeignKey(
#         City,
#         chained_field='country',
#         chained_model_field='country',
#         show_all=False,
#         auto_choose=True,
#         sort=True
#     )


class Company(models.Model):
    CHOICES = [
        ('<10', '<10'),
        ('10-20', '10-20'),
        ('20-50', '20-50'),
        ('50+', '50+'),
        ('100+', '500+')
    ]

    name = models.CharField(max_length=200, unique=True)
    industry = models.ForeignKey('Industry', on_delete=models.CASCADE, null=True, blank=True)
    technologies = models.ManyToManyField('Technology', blank=True)
    established_year = models.IntegerField(validators=[MinValueValidator(1980), max_value_current_year], null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    company_size = models.CharField(max_length=10, choices=CHOICES, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    url = models.URLField(default="", null=True, blank=True)


class Technology(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Industry(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
