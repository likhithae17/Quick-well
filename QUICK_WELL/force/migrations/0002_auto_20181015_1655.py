# Generated by Django 2.1.2 on 2018-10-15 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('force', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equationlog',
            name='userlogid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='force.userLog'),
        ),
    ]
