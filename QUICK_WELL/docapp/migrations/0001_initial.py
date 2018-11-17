# Generated by Django 2.1.3 on 2018-11-15 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('appoint_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Appointment_Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=150)),
                ('lastname', models.CharField(max_length=150)),
                ('experience', models.FloatField(null=True)),
                ('doc_photo', models.CharField(blank=True, max_length=500, null=True)),
                ('email_id', models.CharField(blank=True, max_length=150, null=True)),
                ('phone_num', models.BigIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital_Affiliation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hosp_name', models.CharField(max_length=200)),
                ('hosp_photo', models.CharField(blank=True, max_length=500, null=True)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('country', models.CharField(blank=True, max_length=100)),
                ('address', models.CharField(blank=True, max_length=300)),
                ('start_date', models.DateField(blank=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('doc_name', models.ManyToManyField(default='', null=True, to='docapp.Doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_fee', models.FloatField()),
                ('followup_fee', models.FloatField()),
                ('street_address', models.CharField(blank=True, max_length=500)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('state', models.CharField(blank=True, max_length=100)),
                ('country', models.CharField(blank=True, max_length=100)),
                ('zip', models.BigIntegerField(blank=True)),
                ('doc_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='docapp.Doctor')),
                ('hosp_affiliation_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='docapp.Hospital_Affiliation')),
            ],
        ),
        migrations.CreateModel(
            name='Office_Docavailability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_slot_per_patient', models.FloatField(blank=True, null=True)),
                ('slot1', models.TimeField(default='9:00')),
                ('slot1_available', models.BooleanField(default=True)),
                ('slot2', models.TimeField(default='9:30')),
                ('slot2_available', models.BooleanField(default=True)),
                ('day', models.CharField(max_length=20)),
                ('reason_unavailability', models.CharField(blank=True, max_length=500, null=True)),
                ('office_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='docapp.Office')),
            ],
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qual_name', models.CharField(max_length=500)),
                ('institute_name', models.CharField(max_length=500, null=True)),
                ('procurement_year', models.DateField()),
                ('doc_name', models.ManyToManyField(to='docapp.Doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spec_name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=150)),
                ('lastname', models.CharField(max_length=150)),
                ('age', models.FloatField()),
                ('dob', models.DateField(null=True)),
                ('email', models.CharField(max_length=150)),
                ('contact_number', models.BigIntegerField()),
                ('street_address', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('zip', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User_Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_anonymous', models.BooleanField(default=False)),
                ('wait_time_rating', models.FloatField(null=True)),
                ('manner_rating', models.FloatField(null=True)),
                ('rating', models.FloatField(null=True)),
                ('review', models.CharField(max_length=500, null=True)),
                ('is_doc_recommended', models.BooleanField(default=True)),
                ('review_date', models.DateField()),
                ('client_accountid', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='docapp.User')),
                ('doc_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='docapp.Doctor')),
            ],
        ),
        migrations.AddField(
            model_name='doctor',
            name='spec',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='docapp.Specialization'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='appoint_status_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='docapp.Appointment_Status'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='client_accountid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='docapp.User'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='office_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='docapp.Doctor'),
        ),
    ]
