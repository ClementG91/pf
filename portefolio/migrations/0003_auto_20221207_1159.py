# Generated by Django 4.0.6 on 2022-12-07 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portefolio', '0002_auto_20221207_1154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='author',
        ),
    ]
