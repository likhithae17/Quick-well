# Generated by Django 2.1.2 on 2018-11-10 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('force', '0005_auto_20181110_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='dob',
            field=models.DateField(null=True),
        ),
    ]