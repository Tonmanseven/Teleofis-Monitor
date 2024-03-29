from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190610_1455'),
    ]

    operations = [
        migrations.CreateModel(
            name='telemetry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vin', models.CharField(db_index=True, default=None, max_length=150)),
                ('timetel', models.DateTimeField(default=django.utils.timezone.now)),
                ('cpu_temp', models.CharField(db_index=True, default=None, max_length=150)),
                ('board_temp', models.CharField(db_index=True, default=None, max_length=150)),
            ],
        ),
    ]
