# Generated by Django 5.0.4 on 2024-04-24 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gas_utility', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicerequest',
            name='resolved_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
