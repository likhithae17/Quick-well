# Generated by Django 2.1.3 on 2018-11-17 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docapp', '0007_auto_20181117_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='office_docavailability',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]