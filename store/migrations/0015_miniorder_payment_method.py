# Generated by Django 3.0.7 on 2020-07-30 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_auto_20200727_1157'),
    ]

    operations = [
        migrations.AddField(
            model_name='miniorder',
            name='payment_method',
            field=models.CharField(default='Online by card', max_length=30),
        ),
    ]