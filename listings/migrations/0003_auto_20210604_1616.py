# Generated by Django 3.2.3 on 2021-06-04 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_rename_descriptiom_listing_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='description',
        ),
        migrations.AddField(
            model_name='listing',
            name='descriptiom',
            field=models.TextField(blank=True),
        ),
    ]