# Generated by Django 2.2.9 on 2020-08-13 11:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0030_auto_20200812_1817'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='This_Season',
            new_name='Season_board_1',
        ),
        migrations.RenameModel(
            old_name='Previous_Season',
            new_name='Season_board_2',
        ),
        migrations.AlterField(
            model_name='event_reservation',
            name='created_at',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 8, 13, 13, 43, 29, 329985)),
        ),
        migrations.AlterField(
            model_name='recruitment',
            name='season',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 8, 13, 13, 43, 29, 329985)),
        ),
    ]
