# Generated by Django 2.1.2 on 2018-12-08 18:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_merge_20181208_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='user_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
