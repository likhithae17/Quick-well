# Generated by Django 2.1.2 on 2018-12-06 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_user_reports'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_reports',
            name='file',
            field=models.FileField(blank=True, upload_to='media'),
        ),
    ]
