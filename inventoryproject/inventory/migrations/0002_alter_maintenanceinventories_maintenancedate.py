# Generated by Django 4.1.5 on 2023-01-27 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintenanceinventories',
            name='maintenanceDate',
            field=models.DateField(max_length=11),
        ),
    ]