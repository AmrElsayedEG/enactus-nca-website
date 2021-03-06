# Generated by Django 2.2.9 on 2020-06-28 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='This_Season',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=10)),
                ('last_name', models.CharField(max_length=10)),
                ('role', models.CharField(choices=[('president', 'president'), ('vice president 1', 'vice president 1'), ('vice president 2', 'vice president 2'), ('multimedia director', 'multimedia director')], max_length=2)),
                ('season', models.IntegerField()),
                ('img', models.ImageField(upload_to='members-imgs')),
            ],
        ),
    ]
