# Generated by Django 5.0 on 2023-12-22 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_characterinfo_age_characterinfo_quote_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='characterinfo',
            old_name='character',
            new_name='seriesName',
        ),
    ]