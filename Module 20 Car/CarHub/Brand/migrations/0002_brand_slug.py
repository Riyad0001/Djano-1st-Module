# Generated by Django 4.0.10 on 2024-11-17 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Brand', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
