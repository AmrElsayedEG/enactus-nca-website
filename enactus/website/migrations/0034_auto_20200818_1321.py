# Generated by Django 2.2.9 on 2020-08-18 11:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0033_auto_20200818_1318'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 8, 18, 13, 21, 29, 688102)),
        ),
        migrations.AlterField(
            model_name='event_reservation',
            name='created_at',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 8, 18, 13, 21, 29, 680066)),
        ),
    ]
