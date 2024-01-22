# Generated by Django 5.0 on 2023-12-30 13:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_usercontent_userimage'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userimage',
            name='user',
        ),
        migrations.CreateModel(
            name='UserSeries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createName', models.CharField(max_length=255)),
                ('about', models.TextField(blank=True)),
                ('link', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='app/static/photos/icons')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='UserContent',
        ),
        migrations.DeleteModel(
            name='UserImage',
        ),
    ]
