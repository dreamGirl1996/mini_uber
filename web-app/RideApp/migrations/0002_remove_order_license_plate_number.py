# Generated by Django 3.0.2 on 2020-01-29 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RideApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='license_plate_number',
        ),
    ]
