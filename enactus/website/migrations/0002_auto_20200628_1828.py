# Generated by Django 2.2.9 on 2020-06-28 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='this_season',
            name='role',
            field=models.CharField(choices=[('president', 'president'), ('vice president 1', 'vice president 1'), ('vice president 2', 'vice president 2'), ('multimedia director', 'multimedia director')], max_length=50),
        ),
    ]
