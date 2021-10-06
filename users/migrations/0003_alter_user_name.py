# Generated by Django 3.2.7 on 2021-10-03 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20211003_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(help_text='Full name/alias/nickname as you would usually sign your emails, e.g. John Johnson or Lord Demogorgon.', max_length=255, verbose_name='Name'),
        ),
    ]