# Generated by Django 2.2.2 on 2019-06-10 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190423_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telelog',
            name='log_time',
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterField(
            model_name='teleping',
            name='timestamp',
            field=models.DateTimeField(default=None),
        ),
    ]
