# Generated by Django 3.1.6 on 2021-02-18 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_company_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='technologies',
        ),
        migrations.AddField(
            model_name='company',
            name='technologies',
            field=models.ManyToManyField(to='companies.Technology'),
        ),
    ]
