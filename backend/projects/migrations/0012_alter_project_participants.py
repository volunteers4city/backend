# Generated by Django 4.2.6 on 2023-11-05 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_alter_project_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='participants',
            field=models.ManyToManyField(blank=True, related_name='projects', to='projects.projectparticipants', verbose_name='Участники'),
        ),
    ]