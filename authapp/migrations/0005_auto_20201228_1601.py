# Generated by Django 3.1.3 on 2020-12-28 13:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0004_auto_20201228_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 30, 13, 1, 26, 354163, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]