# Generated by Django 5.0 on 2023-12-22 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_seriesname_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seriesname',
            name='image',
            field=models.ImageField(upload_to='app/static/photos/icons'),
        ),
    ]
