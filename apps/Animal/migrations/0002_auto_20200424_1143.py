# Generated by Django 3.0.5 on 2020-04-24 16:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Animal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='Fecha_recibida',
            field=models.DateField(default=datetime.datetime(2020, 4, 24, 16, 43, 37, 410711, tzinfo=utc)),
        ),
    ]