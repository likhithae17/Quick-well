# Generated by Django 2.1.3 on 2018-11-16 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('med', '0012_auto_20181116_2201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchaseitem',
            name='user',
        ),
    ]