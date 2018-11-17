# Generated by Django 2.1.2 on 2018-11-17 15:14

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
                ('slot2', models.TimeField(default='9:15')),
                ('slot2_available', models.BooleanField(default=True)),
                ('slot3', models.TimeField(default='9:30')),
                ('slot3_available', models.BooleanField(default=True)),
                ('slot4', models.TimeField(default='9:45')),
                ('slot4_available', models.BooleanField(default=True)),
                ('slot5', models.TimeField(default='10:00')),
                ('slot5_available', models.BooleanField(default=True)),
                ('slot6', models.TimeField(default='10:15')),
                ('slot6_available', models.BooleanField(default=True)),
                ('slot7', models.TimeField(default='10:30')),
                ('slot7_available', models.BooleanField(default=True)),
                ('slot8', models.TimeField(default='10:45')),
                ('slot8_available', models.BooleanField(default=True)),
                ('slot9', models.TimeField(default='11:00')),
                ('slot9_available', models.BooleanField(default=True)),
                ('slot10', models.TimeField(default='11:15')),
                ('slot10_available', models.BooleanField(default=True)),
                ('slot11', models.TimeField(default='11:30')),
                ('slot11_available', models.BooleanField(default=True)),
                ('slot12', models.TimeField(default='11:45')),
                ('slot12_available', models.BooleanField(default=True)),
                ('slot13', models.TimeField(default='12:00')),
                ('slot13_available', models.BooleanField(default=True)),
                ('slot14', models.TimeField(default='12:15')),
                ('slot14_available', models.BooleanField(default=True)),
                ('slot15', models.TimeField(default='12:30')),
                ('slot15_available', models.BooleanField(default=True)),
                ('slot16', models.TimeField(default='12:45')),
                ('slot16_available', models.BooleanField(default=True)),
                ('slot17', models.TimeField(default='13:00')),
                ('slot17_available', models.BooleanField(default=True)),
                ('slot18', models.TimeField(default='13:15')),
                ('slot18_available', models.BooleanField(default=True)),
                ('slot19', models.TimeField(default='13:30')),
                ('slot19_available', models.BooleanField(default=True)),
                ('slot20', models.TimeField(default='13:45')),
                ('slot20_available', models.BooleanField(default=True)),
                ('slot21', models.TimeField(default='14:00')),
                ('slot21_available', models.BooleanField(default=True)),
                ('slot22', models.TimeField(default='14:15')),
                ('slot22_available', models.BooleanField(default=True)),
                ('slot23', models.TimeField(default='14:30')),
                ('slot23_available', models.BooleanField(default=True)),
                ('slot24', models.TimeField(default='14:45')),
                ('slot24_available', models.BooleanField(default=True)),
                ('slot25', models.TimeField(default='15:00')),
                ('slot25_available', models.BooleanField(default=True)),
                ('slot26', models.TimeField(default='15:15')),
                ('slot26_available', models.BooleanField(default=True)),
                ('slot27', models.TimeField(default='15:30')),
                ('slot27_available', models.BooleanField(default=True)),
                ('slot28', models.TimeField(default='15:45')),
                ('slot28_available', models.BooleanField(default=True)),
                ('slot29', models.TimeField(default='16:00')),
                ('slot29_available', models.BooleanField(default=True)),
                ('slot30', models.TimeField(default='16:15')),
                ('slot30_available', models.BooleanField(default=True)),
                ('slot31', models.TimeField(default='16:30')),
                ('slot31_available', models.BooleanField(default=True)),
                ('slot32', models.TimeField(default='16:45')),
                ('slot32_available', models.BooleanField(default=True)),
                ('slot33', models.TimeField(default='17:00')),
                ('slot33_available', models.BooleanField(default=True)),
                ('slot34', models.TimeField(default='17:15')),
                ('slot34_available', models.BooleanField(default=True)),
                ('slot35', models.TimeField(default='17:30')),
                ('slot35_available', models.BooleanField(default=True)),
                ('slot36', models.TimeField(default='17:45')),
                ('slot36_available', models.BooleanField(default=True)),
                ('slot37', models.TimeField(default='18:00')),
                ('slot37_available', models.BooleanField(default=True)),
                ('slot38', models.TimeField(default='18:15')),
                ('slot38_available', models.BooleanField(default=True)),
                ('slot39', models.TimeField(default='18:30')),
                ('slot39_available', models.BooleanField(default=True)),
                ('slot40', models.TimeField(default='18:45')),
                ('slot40_available', models.BooleanField(default=True)),
                ('slot41', models.TimeField(default='19:00')),
                ('slot41_available', models.BooleanField(default=True)),
                ('slot42', models.TimeField(default='19:15')),
                ('slot42_available', models.BooleanField(default=True)),
                ('slot43', models.TimeField(default='19:30')),
                ('slot43_available', models.BooleanField(default=True)),
                ('slot44', models.TimeField(default='19:45')),
                ('slot44_available', models.BooleanField(default=True)),
                ('slot45', models.TimeField(default='20:00')),
                ('slot45_available', models.BooleanField(default=True)),
                ('slot46', models.TimeField(default='20:15')),
                ('slot46_available', models.BooleanField(default=True)),
                ('slot47', models.TimeField(default='20:30')),
                ('slot47_available', models.BooleanField(default=True)),
                ('slot48', models.TimeField(default='20:45')),
                ('slot48_available', models.BooleanField(default=True)),
                ('slot49', models.TimeField(default='21:00')),
                ('slot49_available', models.BooleanField(default=True)),
                ('slot50', models.TimeField(default='21:15')),
                ('slot50_available', models.BooleanField(default=True)),
                ('slot51', models.TimeField(default='21:30')),
                ('slot51_available', models.BooleanField(default=True)),
                ('slot52', models.TimeField(default='21:45')),
                ('slot53_available', models.BooleanField(default=True)),
                ('slot54', models.TimeField(default='22:00')),
                ('slot54_available', models.BooleanField(default=True)),
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
