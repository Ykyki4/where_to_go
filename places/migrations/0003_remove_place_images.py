# Generated by Django 3.2.16 on 2022-11-01 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_auto_20221101_1428'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='images',
        ),
    ]
