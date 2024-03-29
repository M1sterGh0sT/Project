# Generated by Django 5.0 on 2023-12-21 23:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_product_characterinfo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='app/static/photos')),
                ('about', models.TextField(blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='characterinfo',
            name='character',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='characterName', to='app.charactername'),
        ),
        migrations.AlterField(
            model_name='characterinfo',
            name='image',
            field=models.ImageField(upload_to='app/static/photos'),
        ),
        migrations.AddField(
            model_name='charactername',
            name='series',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='series', to='app.series'),
            preserve_default=False,
        ),
    ]
