# Generated by Django 3.1.3 on 2020-12-28 12:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0003_auto_20201228_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 30, 12, 58, 4, 993164, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]
