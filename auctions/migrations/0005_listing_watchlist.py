# Generated by Django 4.1.6 on 2023-11-26 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_alter_listing_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='watchlist',
            field=models.BooleanField(default=False),
        ),
    ]