import datetime

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from smart_selects.db_fields import ChainedForeignKey


def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


class Country(models.Model):
    name = models.CharField(max_length=255)


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)


class Location(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = ChainedForeignKey(
        City,
        chained_field='country',
        chained_model_field='country',
        show_all=False,
        auto_choose=True,
        sort=True
    )


class Company(models.Model):
    CHOICES = [
        ('<10', '<10'),
        ('10-20', '10-20'),
        ('20-50', '20-50'),
        ('50+', '50+'),
        ('100+', '500+')
    ]

    name = models.CharField(max_length=200, unique=True)
    industry = models.ForeignKey('Industry', on_delete=models.CASCADE)
    technologies = models.ManyToManyField('Technology', null=True)
    established_year = models.IntegerField(validators=[MinValueValidator(2000), max_value_current_year])
    description = models.TextField(null=True)
    company_size = models.CharField(max_length=10, choices=CHOICES)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    url = models.URLField(default="")


class Technology(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Industry(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
