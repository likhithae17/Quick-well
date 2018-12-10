# Generated by Django 2.1.2 on 2018-12-10 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20181210_1720'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clinic',
            name='doc_id',
        ),
        migrations.AddField(
            model_name='clinic',
            name='doc_id',
            field=models.ManyToManyField(blank=True, default='', null=True, to='home.Doctor'),
        ),
    ]
