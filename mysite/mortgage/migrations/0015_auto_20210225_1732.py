# Generated by Django 2.0.7 on 2021-02-25 22:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mortgage', '0014_auto_20210225_0958'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image_Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='monthly_expenses',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2021, 2, 25, 22, 32, 12, 175648, tzinfo=utc)),
        ),
    ]
