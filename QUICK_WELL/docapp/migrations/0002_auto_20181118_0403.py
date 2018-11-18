# Generated by Django 2.1.3 on 2018-11-17 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LabTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lab_name', models.CharField(max_length=150)),
                ('lab_photo', models.FileField(blank=True, null=True, upload_to='')),
                ('email_id', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone_num', models.BigIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tests_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(max_length=150)),
                ('preparation', models.TextField()),
                ('procedure', models.TextField()),
                ('cost', models.FloatField()),
            ],
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='appoint_date',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='appoint_status_id',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='client_accountid',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='start_time',
        ),
        migrations.AddField(
            model_name='appointment',
            name='appointment_id',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appointment',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='email_id',
            field=models.EmailField(default=None, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appointment',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='user_name',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='doctor',
            name='experience',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='hospital_affiliation',
            name='doc_name',
            field=models.ManyToManyField(default='', to='docapp.Doctor'),
        ),
        migrations.AddField(
            model_name='labtest',
            name='tests_available',
            field=models.ManyToManyField(to='docapp.Tests_info'),
        ),
    ]