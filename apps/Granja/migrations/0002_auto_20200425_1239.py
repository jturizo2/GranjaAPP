# Generated by Django 3.0.5 on 2020-04-25 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Granja', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='granja',
            name='Img',
        ),
        migrations.AddField(
            model_name='granja',
            name='image',
            field=models.ImageField(default='gallery/static/images/no-img.jpg', upload_to='gallery/'),
        ),
    ]
