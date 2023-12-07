# Generated by Django 4.2.6 on 2023-12-04 19:04

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_alter_address_address_line_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='date_of_birth',
            field=models.DateField(validators=[django.core.validators.MinValueValidator(limit_value=datetime.date(1900, 1, 1)), django.core.validators.MaxValueValidator(limit_value=datetime.date(2023, 12, 4))], verbose_name='Дата рождения'),
        ),
    ]