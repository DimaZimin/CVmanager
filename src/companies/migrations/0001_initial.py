# Generated by Django 3.1.6 on 2021-02-18 10:40

import companies.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='country', chained_model_field='country', on_delete=django.db.models.deletion.CASCADE, to='companies.city')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.country')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('established_year', models.IntegerField(validators=[django.core.validators.MinValueValidator(2000), companies.models.max_value_current_year])),
                ('description', models.TextField()),
                ('company_size', models.CharField(choices=[('<10', '<10'), ('10-20', '10-20'), ('20-50', '20-50'), ('50+', '50+'), ('100+', '500+')], max_length=10)),
                ('industry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.industry')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.location')),
                ('technologies', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.technology')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.country'),
        ),
    ]
