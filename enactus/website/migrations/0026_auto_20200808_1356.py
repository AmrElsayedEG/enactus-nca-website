# Generated by Django 2.2.9 on 2020-08-08 11:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0025_auto_20200807_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event_reservation',
            name='created_at',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 8, 8, 13, 56, 3, 117548)),
        ),
        migrations.AlterField(
            model_name='recruitment',
            name='college',
            field=models.CharField(choices=[('Computer Science', 'Computer Science'), ('Engineering', 'Engineering'), ('Information Systems', 'Information Systems'), ('Applied Arts', 'Applied Arts'), ('Commerce and Business Administration', 'Commerce and Business Administration')], max_length=50),
        ),
    ]
