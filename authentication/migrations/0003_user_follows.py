# Generated by Django 4.0.6 on 2022-12-07 11:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20221206_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='follows',
            field=models.ManyToManyField(limit_choices_to={'role': 'COWORKER'}, to=settings.AUTH_USER_MODEL, verbose_name='suit'),
        ),
    ]