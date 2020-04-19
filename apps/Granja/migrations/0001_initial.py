# Generated by Django 3.0.5 on 2020-04-19 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='granja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cod', models.CharField(max_length=20)),
                ('Name', models.CharField(max_length=80)),
                ('Details', models.CharField(max_length=500)),
                ('Hec', models.FloatField()),
                ('Div', models.FloatField()),
                ('NumPozos', models.IntegerField()),
                ('Img', models.CharField(max_length=150)),
            ],
        ),
    ]
