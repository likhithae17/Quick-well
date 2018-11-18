

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('docapp', '0003_auto_20181118_0509'),
    ]

    operations = [
        migrations.AddField(
            model_name='office',
            name='lab_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='docapp.LabTest'),
        ),
    ]
