# Generated by Django 3.0.2 on 2020-03-06 01:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200305_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='date_price',
            field=models.DateField(default=datetime.datetime(2020, 3, 5, 21, 9, 51, 854153)),
        ),
        migrations.AlterField(
            model_name='products',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 3, 5, 21, 9, 51, 853153)),
        ),
    ]
