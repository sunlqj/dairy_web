# Generated by Django 4.1.1 on 2024-02-23 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_dairy', '0015_db_dairycontent'),
    ]

    operations = [
        migrations.DeleteModel(
            name='db_DairyContent',
        ),
        migrations.DeleteModel(
            name='db_DairyList',
        ),
    ]
