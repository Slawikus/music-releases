# Generated by Django 3.2.7 on 2021-09-12 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='is_viewed',
            field=models.BooleanField(default=False),
        ),
    ]