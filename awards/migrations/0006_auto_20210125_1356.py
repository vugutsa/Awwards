# Generated by Django 3.1.5 on 2021-01-25 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0005_auto_20210125_1133'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projects',
            old_name='title',
            new_name='project_title',
        ),
    ]
