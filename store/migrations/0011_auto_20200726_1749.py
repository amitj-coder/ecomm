# Generated by Django 3.0.7 on 2020-07-26 12:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_auto_20200726_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='miniorder',
            name='return_window',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 5, 12, 19, 47, 155821, tzinfo=utc)),
        ),
    ]
