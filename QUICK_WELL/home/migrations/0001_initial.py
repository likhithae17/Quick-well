# Generated by Django 2.1.2 on 2018-12-08 21:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('email_id', models.EmailField(max_length=254)),
                ('date', models.DateField(blank=True, null=True)),
                ('time', models.TimeField(blank=True, null=True)),
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
                ('experience', models.IntegerField(null=True)),
                ('doc_photo', models.FileField(null=True, upload_to='')),
                ('phone_num', models.BigIntegerField(blank=True, null=True)),
                ('specialization', models.CharField(max_length=150, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='fundraiser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('Title', models.CharField(max_length=60)),
                ('goal_amount', models.FloatField()),
                ('beneficiary_name', models.CharField(max_length=50)),
                ('beneficiary_relation', models.CharField(max_length=25)),
                ('Fundraiser_story', models.TextField()),
                ('End_date', models.DateField()),
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
                ('doc_name', models.ManyToManyField(default='', to='home.Doctor')),
            ],
        ),
        migrations.CreateModel(
            name='labAppointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('email_id', models.EmailField(max_length=254)),
                ('date', models.DateField(blank=True, null=True)),
                ('time', models.TimeField(blank=True, null=True)),
            ],
        ),
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
            name='Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('pharmacy', models.CharField(max_length=100)),
                ('about', models.CharField(default='0000000', max_length=1000)),
                ('description', models.ImageField(blank=True, upload_to='')),
                ('mfg_date', models.DateField(null=True)),
                ('exp_date', models.DateField(null=True)),
                ('pres_req', models.CharField(max_length=100)),
                ('price', models.FloatField()),
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
                ('doc_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='home.Doctor')),
                ('hosp_affiliation_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='home.Hospital_Affiliation')),
            ],
        ),
        migrations.CreateModel(
            name='Office_Docavailability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_slot_per_patient', models.FloatField(blank=True, null=True)),
                ('day', models.CharField(max_length=20)),
                ('reason_unavailability', models.CharField(blank=True, max_length=500, null=True)),
                ('office_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.Office')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref_code', models.CharField(max_length=15)),
                ('is_ordered', models.BooleanField(default=False)),
                ('date_ordered', models.DateTimeField(null=True)),
                ('billing_add', models.CharField(blank=True, max_length=1000)),
                ('email', models.CharField(default='0000000', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref_code', models.CharField(default='0000000', max_length=15)),
                ('quantity', models.IntegerField(null=True)),
                ('is_ordered', models.BooleanField(default=False)),
                ('date_added', models.DateTimeField(null=True)),
                ('date_ordered', models.DateTimeField(null=True)),
                ('medicine', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Medicine', unique=None)),
            ],
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qual_name', models.CharField(max_length=500)),
                ('institute_name', models.CharField(max_length=500, null=True)),
                ('procurement_year', models.DateField()),
                ('doc_name', models.ManyToManyField(to='home.Doctor')),
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
                ('username', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='user_reports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, upload_to='media')),
                ('username', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
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
                ('client_accountid', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.user_profile')),
                ('doc_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.Doctor')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='0000000', max_length=100)),
                ('last_name', models.CharField(default='0000000', max_length=100)),
                ('email', models.CharField(default='0000000', max_length=100)),
                ('address', models.CharField(blank=True, max_length=1000)),
                ('city', models.CharField(default='', max_length=200)),
                ('medicine', models.ManyToManyField(blank=True, to='home.Medicine')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='home.PurchaseItem'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.UserProfile'),
        ),
        migrations.AddField(
            model_name='labtest',
            name='tests_available',
            field=models.ManyToManyField(to='home.Tests_info'),
        ),
        migrations.AddField(
            model_name='labappointment',
            name='test_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.Tests_info'),
        ),
        migrations.AddField(
            model_name='fundraiser',
            name='user_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='home.user_profile'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='doctor_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='home.Doctor'),
        ),
    ]
