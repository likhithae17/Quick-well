
<<<<<<< HEAD
# Generated by Django 2.1.2 on 2018-11-18 07:23
=======
# Generated by Django 2.1.3 on 2018-11-18 10:24
# Generated by Django 2.1.2 on 2018-11-18 07:23

>>>>>>> dabd294b24d99e283e35516cb127cb2996155fd7

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='video_con_pass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_conference', models.DateTimeField(default=django.utils.timezone.now)),
                ('conference_link', models.CharField(max_length=120)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='video_con_request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_requested', models.DateTimeField(auto_now_add=True)),
<<<<<<< HEAD
                ('requeste_id', models.CharField(max_length=120)),
                ('request_id', models.CharField(max_length=12)),
=======

                ('requeste_id', models.CharField(max_length=120)),
                ('request_id', models.CharField(max_length=12)),

>>>>>>> dabd294b24d99e283e35516cb127cb2996155fd7
                ('requester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
