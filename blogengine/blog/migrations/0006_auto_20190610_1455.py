# Generated by Django 2.2.2 on 2019-06-10 14:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190610_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telelog',
            name='log_name',
            field=models.CharField(db_index=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='telelog',
            name='log_text',
            field=models.TextField(db_index=True),
        ),
        migrations.AlterField(
            model_name='telelog',
            name='log_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='teleping',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
