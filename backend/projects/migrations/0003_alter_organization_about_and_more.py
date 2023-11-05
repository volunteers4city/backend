# Generated by Django 4.2.6 on 2023-11-04 08:39

import datetime
import django.core.validators
from django.db import migrations, models
import projects.validators


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_volunteer_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='about',
            field=models.TextField(blank=True, max_length=750, validators=[projects.validators.validate_about], verbose_name='Об организации'),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='date_of_birth',
            field=models.DateField(help_text='Введите дату в формате "ГГГГ.ММ.ДД", пример: "2000 01 01".', validators=[django.core.validators.MinValueValidator(limit_value=datetime.date(1900, 1, 1)), django.core.validators.MaxValueValidator(limit_value=datetime.date(2023, 11, 4))], verbose_name='Дата рождения'),
        ),
    ]