# Generated by Django 3.0.7 on 2020-07-27 06:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_auto_20200726_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='miniorder',
            name='return_window',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 6, 6, 26, 35, 153632, tzinfo=utc)),
        ),
    ]
