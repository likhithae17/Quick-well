# Generated by Django 2.1.2 on 2018-11-10 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('force', '0008_auto_20181110_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='photo',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
    ]
