# Generated by Django 2.2.9 on 2020-08-07 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_recruitment_season'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Events',
            new_name='Event',
        ),
        migrations.RenameModel(
            old_name='album_cover',
            new_name='Gallery',
        ),
    ]
