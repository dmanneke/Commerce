# Generated by Django 4.2.3 on 2023-07-10 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_listing_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='time',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
