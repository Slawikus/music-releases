# Generated by Django 3.2.5 on 2021-08-01 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('releases', '0006_merge_20210801_1146'),
    ]

    operations = [
        migrations.RenameField(
            model_name='release',
            old_name='release_date',
            new_name='submitted_at',
        ),
    ]