# Generated by Django 2.2.2 on 2019-06-10 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190610_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telelog',
            name='log_name',
            field=models.CharField(db_index=True, default=None, max_length=150),
        ),
    ]
