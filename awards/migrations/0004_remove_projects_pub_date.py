# Generated by Django 3.1.5 on 2021-01-24 22:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0003_auto_20210124_2352'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='pub_date',
        ),
    ]
