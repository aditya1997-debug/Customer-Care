# Generated by Django 4.0.4 on 2023-08-23 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gas_service_app', '0021_message_related_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicerequest',
            name='status',
            field=models.CharField(choices=[('Submitted', 'Submitted'), ('Pending', 'Pending'), ('Resolved', 'Resolved')], default='Submitted', max_length=20),
        ),
    ]
