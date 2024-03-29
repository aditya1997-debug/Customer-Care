# Generated by Django 4.0.4 on 2023-08-12 06:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gas_service_app', '0004_remove_customer_account_balance_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(message='Invalid phone number.', regex='^\\d{0,9}$')]),
        ),
    ]
