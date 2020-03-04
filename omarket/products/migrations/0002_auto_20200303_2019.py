# Generated by Django 3.0.2 on 2020-03-04 00:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animal', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Cortes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('corte', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='products',
            name='disponibles',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='products',
            name='animal',
            field=models.ForeignKey(default=1000, on_delete=django.db.models.deletion.CASCADE, to='products.Animales'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='products',
            name='corte',
            field=models.ForeignKey(default=1000, on_delete=django.db.models.deletion.CASCADE, to='products.Cortes'),
            preserve_default=False,
        ),
    ]
