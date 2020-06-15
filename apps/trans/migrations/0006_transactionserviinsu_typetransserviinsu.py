# Generated by Django 3.0.5 on 2020-05-31 13:55

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Granja', '0004_granja_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trans', '0005_transaction_idgranja'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeTransserviInsu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tipo', models.CharField(max_length=30)),
                ('Detalle', models.CharField(max_length=100)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='transactionserviInsu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('detail', models.CharField(max_length=100)),
                ('Value', models.FloatField()),
                ('quantity', models.FloatField()),
                ('Total', models.FloatField()),
                ('IdGranja', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Granja.granja')),
                ('Tipo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='trans.TypeTransserviInsu')),
                ('concepto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='trans.serviInsu')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
