# Generated by Django 3.0.8 on 2020-11-21 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0004_auto_20201121_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='bed',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='patient',
            name='venti',
            field=models.CharField(max_length=64),
        ),
    ]