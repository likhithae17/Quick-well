# Generated by Django 2.1.3 on 2018-12-11 18:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20181211_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_review',
            name='review_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 11, 18, 20, 33, 512501)),
        ),
    ]
