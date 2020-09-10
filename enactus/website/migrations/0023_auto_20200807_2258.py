# Generated by Django 2.2.9 on 2020-08-07 20:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0022_auto_20200807_2244'),
    ]

    operations = [
        migrations.AddField(
            model_name='summary',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='history-imgs'),
        ),
        migrations.AddField(
            model_name='summary',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='event_reservation',
            name='created_at',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 8, 7, 22, 58, 33, 946481)),
        ),
    ]
