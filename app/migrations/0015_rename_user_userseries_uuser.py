# Generated by Django 5.0 on 2023-12-30 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_remove_userimage_user_userseries_delete_usercontent_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userseries',
            old_name='user',
            new_name='uuser',
        ),
    ]
