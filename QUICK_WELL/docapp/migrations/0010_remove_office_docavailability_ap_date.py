# Generated by Django 2.1.3 on 2018-11-17 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('docapp', '0009_auto_20181117_1323'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='office_docavailability',
            name='ap_date',
        ),
    ]
