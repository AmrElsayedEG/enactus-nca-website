# Generated by Django 2.2.9 on 2020-06-28 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_event_reservation'),
    ]

    operations = [
        migrations.AddField(
            model_name='event_reservation',
            name='phone',
            field=models.CharField(default='00000000000', max_length=15),
        ),
    ]
