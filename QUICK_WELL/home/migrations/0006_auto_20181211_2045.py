# Generated by Django 2.1.2 on 2018-12-11 15:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20181211_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_review',
            name='review_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 11, 20, 45, 28, 210369)),
        ),
    ]
