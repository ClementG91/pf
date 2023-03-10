# Generated by Django 4.0.6 on 2022-12-07 10:54

from django.db import migrations

def migrate_author_to_contributors(apps, schema_editor):
    Blog = apps.get_model('portefolio', 'Blog')
    for blog in Blog.objects.all():
        if blog.author:
            blog.contributors.add(
                blog.author, through_defaults={'contribution': 'Auteur principal'})


class Migration(migrations.Migration):

    dependencies = [
        ('portefolio', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(migrate_author_to_contributors)
    ]
