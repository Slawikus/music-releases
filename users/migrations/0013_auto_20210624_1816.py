# Generated by Django 3.2 on 2021-06-24 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20210624_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='currency',
            field=models.IntegerField(blank=True, choices=[(1, 'D'), (2, 'S'), (3, 'H')], null=True),
        ),
        migrations.DeleteModel(
            name='ProfileCurrency',
        ),
    ]
