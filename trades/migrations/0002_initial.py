# Generated by Django 3.2.8 on 2021-10-17 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('trades', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertraderequest',
            name='from_profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sent_trade_requests', to='users.profile'),
        ),
        migrations.AddField(
            model_name='usertraderequest',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_trade_requests', to='users.profile'),
        ),
    ]
