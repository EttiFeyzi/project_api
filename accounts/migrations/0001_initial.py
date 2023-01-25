# Generated by Django 4.1.5 on 2023-01-21 04:33

import accounts.models
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OTPRequest',
            fields=[
                ('request_id', models.UUIDField(default=uuid.UUID('23b1075e-8b8d-4db3-ad21-eee8bba63ffa'), editable=False, primary_key=True, serialize=False)),
                ('phone', models.CharField(max_length=30, verbose_name='تلفن')),
                ('code', models.CharField(default=accounts.models.generate_otp, max_length=30, verbose_name='کد')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ساخت')),
            ],
            options={
                'verbose_name': 'درخواست otp',
                'verbose_name_plural': 'درخواست otp',
            },
        ),
    ]
