# Generated by Django 2.1.3 on 2018-12-08 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20181208_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='doctor_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='home.Doctor'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='specialization',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='fundraiser',
            name='user_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='home.user_profile'),
        ),
    ]