# Generated by Django 3.2.7 on 2021-09-21 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_label_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='label',
            name='is_main',
            field=models.BooleanField(default=False),
        ),
    ]
