# Generated by Django 2.1.3 on 2018-11-16 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('med', '0013_remove_purchaseitem_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_ordered',
            field=models.DateField(),
        ),
    ]
