# Generated by Django 5.0.3 on 2024-03-24 10:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_blood_stock_hospital_add_blood_stock_hospital_num'),
    ]

    operations = [
        migrations.CreateModel(
            name='BloodDonor_hospitals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hos_name', models.CharField(max_length=100)),
                ('hos_place', models.CharField(max_length=255)),
                ('posted_date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('hos_contact', models.IntegerField(null=True)),
                ('blood_need', models.CharField(max_length=10)),
            ],
        ),
    ]
