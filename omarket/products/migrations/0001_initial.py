# Generated by Django 3.0.2 on 2020-03-05 09:05

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animalName', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Cuts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cutName', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Pieces',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pieceName', models.CharField(max_length=30)),
                ('piece_product', models.ManyToManyField(to='products.Animals')),
                ('cut_piece', models.ManyToManyField(to='products.Cuts')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prodName', models.CharField(max_length=30)),
                ('quantity', models.IntegerField(default=0)),
                ('exempt', models.BooleanField(default=False)),
                ('date', models.DateField(default=datetime.datetime(2020, 3, 5, 5, 5, 11, 785057))),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('piece_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Pieces')),
                ('animal_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Animals')),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('date_price', models.DateField(default=datetime.datetime(2020, 3, 5, 5, 5, 11, 785057))),
                ('price_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Products')),
            ],
        ),
    ]
