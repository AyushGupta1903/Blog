# Generated by Django 4.0.3 on 2022-05-29 08:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0016_alter_blogs_database_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs_database',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 29, 8, 24, 56, 415881)),
        ),
    ]