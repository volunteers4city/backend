# Generated by Django 4.2.6 on 2023-11-04 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_alter_feedback_email_alter_platformabout_about_us_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skills',
            name='name',
            field=models.CharField(max_length=250, unique=True, verbose_name='Навык'),
        ),
    ]
