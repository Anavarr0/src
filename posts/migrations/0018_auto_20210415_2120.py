# Generated by Django 3.0.2 on 2021-04-15 21:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0017_auto_20210415_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='expiration_time',
            field=models.DurationField(default=datetime.timedelta(0, 300)),
        ),
    ]