# Generated by Django 4.0.10 on 2024-09-02 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catagory', '0002_remove_catmodel_tasks'),
    ]

    operations = [
        migrations.RenameField(
            model_name='catmodel',
            old_name='catagory_name',
            new_name='name',
        ),
    ]
