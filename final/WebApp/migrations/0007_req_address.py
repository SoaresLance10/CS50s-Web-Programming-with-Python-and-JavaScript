# Generated by Django 3.0.8 on 2020-11-21 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0006_req'),
    ]

    operations = [
        migrations.AddField(
            model_name='req',
            name='address',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
    ]