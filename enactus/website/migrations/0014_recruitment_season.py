# Generated by Django 2.2.9 on 2020-08-07 17:05

from django.db import migrations, models
import website.models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_recruitment'),
    ]

    operations = [
        migrations.AddField(
            model_name='recruitment',
            name='season',
            field=models.IntegerField(default=website.models.recruitment.current_year, verbose_name='year'),
        ),
    ]
