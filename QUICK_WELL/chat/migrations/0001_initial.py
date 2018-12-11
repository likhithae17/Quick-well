<<<<<<< HEAD
# Generated by Django 2.1.3 on 2018-12-11 18:16
=======
# Generated by Django 2.1.2 on 2018-12-11 20:04
>>>>>>> 4ada355f9f67198969126c28466015d8222c8c9d

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
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('roomname', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_messages', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Patientdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientname', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('symptoms', models.CharField(max_length=250)),
                ('Department', models.CharField(max_length=250)),
            ],
        ),
    ]
