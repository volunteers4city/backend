# Generated by Django 4.2.6 on 2023-11-06 00:48

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import projects.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0014_alter_project_participants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='contact_person',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='organization', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(validators=[projects.validators.regex_string_validator, projects.validators.LengthValidator(max_length=750, min_length=10)], verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='project',
            name='event_purpose',
            field=models.TextField(validators=[projects.validators.regex_string_validator, projects.validators.LengthValidator(max_length=750, min_length=10)], verbose_name='Цель проекта'),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=100, unique=True, validators=[projects.validators.validate_name], verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='project',
            name='organizer_provides',
            field=models.TextField(blank=True, validators=[projects.validators.regex_string_validator, projects.validators.LengthValidator(max_length=750, min_length=2)], verbose_name='Организатор предоставляет'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_events',
            field=models.TextField(validators=[projects.validators.regex_string_validator, projects.validators.LengthValidator(max_length=750, min_length=2)], verbose_name='Мероприятия на проекте'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_tasks',
            field=models.TextField(validators=[projects.validators.regex_string_validator, projects.validators.LengthValidator(max_length=750, min_length=2)], verbose_name='Задачи проекта'),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='date_of_birth',
            field=models.DateField(help_text='Введите дату в формате "ГГГГ-ММ-ДД", пример: "2000-01-01".', validators=[django.core.validators.MinValueValidator(limit_value=datetime.date(1900, 1, 1)), django.core.validators.MaxValueValidator(limit_value=datetime.date(2023, 11, 6))], verbose_name='Дата рождения'),
        ),
    ]