# Generated by Django 4.2.3 on 2023-07-10 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_category_listing_wachtlist_iscategory_comment_bid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category',
            new_name='name',
        ),
    ]
