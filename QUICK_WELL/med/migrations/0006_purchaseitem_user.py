# Generated by Django 2.1.3 on 2018-11-16 14:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('med', '0005_auto_20181116_0116'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseitem',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
