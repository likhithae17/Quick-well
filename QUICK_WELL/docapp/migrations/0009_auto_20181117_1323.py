# Generated by Django 2.1.3 on 2018-11-17 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('docapp', '0008_auto_20181117_1316'),
    ]

    operations = [
        migrations.RenameField(
            model_name='office_docavailability',
            old_name='date',
            new_name='ap_date',
        ),
    ]
