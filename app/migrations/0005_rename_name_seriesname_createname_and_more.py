# Generated by Django 5.0 on 2023-12-22 15:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_seriesname_remove_charactername_series_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seriesname',
            old_name='name',
            new_name='createName',
        ),
        migrations.AlterField(
            model_name='characterinfo',
            name='character',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='series', to='app.seriesname'),
        ),
    ]
