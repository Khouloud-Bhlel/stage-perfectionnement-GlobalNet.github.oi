# Generated by Django 4.2.4 on 2023-08-06 22:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0004_remove_client_cinclientexistant_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='captcha',
        ),
    ]
