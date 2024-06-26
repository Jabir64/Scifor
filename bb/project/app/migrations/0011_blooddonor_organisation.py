# Generated by Django 5.0.3 on 2024-03-24 10:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_blooddonor_hospitals'),
    ]

    operations = [
        migrations.CreateModel(
            name='BloodDonor_organisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_name', models.CharField(max_length=50)),
                ('org_place', models.CharField(max_length=50)),
                ('posted_date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('org_contact', models.IntegerField(null=True)),
                ('blood_need', models.CharField(max_length=10)),
            ],
        ),
    ]
