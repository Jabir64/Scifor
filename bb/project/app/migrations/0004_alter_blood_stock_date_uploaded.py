# Generated by Django 5.0.2 on 2024-03-23 20:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_blood_stock_date_uploaded'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blood_stock',
            name='date_uploaded',
            field=models.DateField(default=datetime.date.today, verbose_name='Date Uploaded'),
        ),
    ]