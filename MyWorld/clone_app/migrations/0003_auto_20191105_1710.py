# Generated by Django 2.2.5 on 2019-11-05 11:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clone_app', '0002_auto_20191104_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 5, 11, 40, 8, 502060, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 5, 11, 40, 8, 501029, tzinfo=utc)),
        ),
    ]
