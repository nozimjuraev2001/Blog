# Generated by Django 4.1.3 on 2022-11-27 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_api', '0002_alter_postmodel_author_alter_postmodel_published_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postmodel',
            name='slug',
        ),
    ]