# Generated by Django 3.2.8 on 2021-10-26 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public_tradelist', '0003_traderequest_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traderequestitem',
            name='trade_points',
            field=models.DecimalField(decimal_places=1, max_digits=3, null=True),
        ),
    ]
