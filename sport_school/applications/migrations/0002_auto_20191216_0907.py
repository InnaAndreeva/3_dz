# Generated by Django 2.2.7 on 2019-12-16 06:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='age',
        ),
        migrations.AddField(
            model_name='application',
            name='birth_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
