# Generated by Django 4.2.3 on 2023-07-10 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_comment_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
