# Generated by Django 3.0.7 on 2020-07-19 08:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20200717_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 19, 8, 42, 9, 523622, tzinfo=utc)),
        ),
    ]