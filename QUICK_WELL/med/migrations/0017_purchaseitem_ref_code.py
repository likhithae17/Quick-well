# Generated by Django 2.1.3 on 2018-11-16 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('med', '0016_auto_20181116_2315'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseitem',
            name='ref_code',
            field=models.CharField(default='0000000', max_length=15),
        ),
    ]