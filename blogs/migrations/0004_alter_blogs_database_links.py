# Generated by Django 4.0.3 on 2022-05-22 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_blogs_database_updated_on_alter_blogs_database_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs_database',
            name='links',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
    ]
