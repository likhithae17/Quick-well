# Generated by Django 2.1.3 on 2018-11-16 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('med', '0011_order_ref_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseitem',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
    ]
