# Generated by Django 5.0 on 2023-12-20 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='CharacterInfo',
        ),
        migrations.RenameModel(
            old_name='Category',
            new_name='CharacterName',
        ),
    ]
