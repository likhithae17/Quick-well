# Generated by Django 2.1.3 on 2018-12-07 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_remove_patientdetails_patient'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Advertiser', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('image', models.FileField(upload_to='')),
                ('link', models.URLField()),
            ],
        ),
    ]