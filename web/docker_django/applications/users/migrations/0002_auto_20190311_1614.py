# Generated by Django 2.0.9 on 2019-03-11 16:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deptemp',
            name='to_date',
            field=models.DateField(default=datetime.datetime(2101, 4, 30, 16, 14, 54, 464474), verbose_name='to'),
        ),
        migrations.AlterField(
            model_name='deptmanager',
            name='to_date',
            field=models.DateField(default=datetime.datetime(2101, 4, 30, 16, 14, 54, 466546), verbose_name='to'),
        ),
    ]
