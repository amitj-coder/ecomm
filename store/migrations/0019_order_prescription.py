# Generated by Django 3.0.7 on 2020-08-02 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_auto_20200731_1922'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='prescription',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.PrescriptionUpload'),
        ),
    ]
