# Generated by Django 5.0.7 on 2024-08-10 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namee', models.CharField(max_length=70)),
                ('about', models.TextField()),
            ],
        ),
    ]