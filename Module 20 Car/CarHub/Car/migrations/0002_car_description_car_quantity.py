# Generated by Django 4.0.10 on 2024-11-19 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Car', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='Description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='Quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]