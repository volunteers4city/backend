# Generated by Django 4.2.6 on 2023-11-03 20:25

import content.validators
import users.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='email',
            field=models.EmailField(max_length=256, validators=[
                                    users.validators.EmailValidator.validate_email], verbose_name='Почтовый адрес'),
        ),
        migrations.AlterField(
            model_name='platformabout',
            name='about_us',
            field=models.TextField(max_length=750, validators=[
                                   content.validators.AboutUsValidator.validate_about_us], verbose_name='Описание раздела "О нас"'),
        ),
        migrations.AlterField(
            model_name='platformabout',
            name='platform_email',
            field=models.EmailField(max_length=256, validators=[
                                    users.validators.EmailValidator.validate_email], verbose_name='email Платформы'),
        ),
    ]
