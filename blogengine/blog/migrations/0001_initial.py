<<<<<<< HEAD
# Generated by Django 2.2 on 2019-04-12 15:01

from django.db import migrations, models
=======
# Generated by Django 2.1.5 on 2019-04-22 11:23

from django.db import migrations, models
import django.utils.timezone
>>>>>>> origin


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
<<<<<<< HEAD
            name='Teleofis_state',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('status', models.BooleanField(db_index=True)),
            ],
            options={
                'db_table': '"teleofis_state"',
            },
=======
            name='telelog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_text', models.TextField(db_index=True)),
                ('log_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('log_name', models.CharField(db_index=True, default=None, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='teleping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(db_index=True, default=None, max_length=150)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('inet', models.BooleanField(db_index=True)),
                ('vpn', models.BooleanField(db_index=True)),
            ],
>>>>>>> origin
        ),
    ]
