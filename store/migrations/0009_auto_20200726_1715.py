# Generated by Django 3.0.7 on 2020-07-26 11:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20200726_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='miniorder',
            name='return_window',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 5, 11, 45, 30, 898421, tzinfo=utc)),
        ),
    ]
