# Generated by Django 5.0 on 2023-12-30 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_rename_user_userseries_uuser'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userseries',
            old_name='uuser',
            new_name='user',
        ),
    ]
