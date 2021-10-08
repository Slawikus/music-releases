# Generated by Django 3.2.7 on 2021-10-08 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('releases', '0001_initial'),
        ('public_tradelist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='traderequestitem',
            name='release',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trade_items', to='releases.release'),
        ),
        migrations.AddField(
            model_name='traderequestitem',
            name='trade_request',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trade_items', to='public_tradelist.traderequest'),
        ),
    ]
