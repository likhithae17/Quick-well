# Generated by Django 2.1.2 on 2018-11-17 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('doctor', models.CharField(max_length=150, null=True)),
                ('age', models.IntegerField()),
                ('email', models.CharField(max_length=150)),
                ('contact_number', models.BigIntegerField()),
                ('specialisations', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='user_profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('age', models.IntegerField(null=True)),
                ('dob', models.DateField(null=True)),
                ('email', models.CharField(max_length=150)),
                ('contact_number', models.BigIntegerField()),
                ('address', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100, null=True)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('zipcode', models.BigIntegerField()),
                ('photo', models.ImageField(blank=True, upload_to='media')),
            ],
        ),
    ]