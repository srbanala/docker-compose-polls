# Generated by Django 2.0.7 on 2021-10-05 14:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mortgage', '0021_auto_20211004_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthly_expenses',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2021, 10, 5, 14, 3, 15, 715167, tzinfo=utc)),
        ),
    ]
