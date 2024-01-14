# Generated by Django 5.0 on 2023-12-22 15:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_series_alter_characterinfo_character_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeriesName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('about', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to='core/static/photos/icons')),
            ],
        ),
        migrations.RemoveField(
            model_name='charactername',
            name='series',
        ),
        migrations.AlterField(
            model_name='characterinfo',
            name='character',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='app.seriesname'),
        ),
        migrations.DeleteModel(
            name='Series',
        ),
        migrations.DeleteModel(
            name='CharacterName',
        ),
    ]