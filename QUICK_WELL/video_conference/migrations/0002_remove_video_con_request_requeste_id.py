# Generated by Django 2.1.3 on 2018-11-18 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video_conference', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video_con_request',
            name='requeste_id',
        ),
    ]
