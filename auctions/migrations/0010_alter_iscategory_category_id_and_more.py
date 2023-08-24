# Generated by Django 4.2.3 on 2023-07-10 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_alter_listing_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iscategory',
            name='category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.category'),
        ),
        migrations.AlterField(
            model_name='iscategory',
            name='listing_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.listing'),
        ),
    ]
