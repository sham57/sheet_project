# Generated by Django 3.2.3 on 2021-06-02 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='descriptiom',
            new_name='description',
        ),
    ]
