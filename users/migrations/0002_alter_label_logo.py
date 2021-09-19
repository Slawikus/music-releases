# Generated by Django 3.2.7 on 2021-09-18 15:48

import configuration.file_storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='label',
            name='logo',
            field=models.ImageField(blank=True, help_text='For best result - black logo on white or transparent background', null=True, storage=configuration.file_storage.DuplicationFixFileSystemStorage(), upload_to='images/labels/', verbose_name='Label logo'),
        ),
    ]