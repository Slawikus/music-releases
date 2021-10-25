# Generated by Django 3.2.8 on 2021-10-17 12:09

import configuration.file_storage
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Label name as you write on your releases', max_length=250, verbose_name='Label name')),
                ('logo', models.ImageField(blank=True, help_text='For best result - black logo on white or transparent background', null=True, storage=configuration.file_storage.DuplicationFixFileSystemStorage(), upload_to='images/labels/', verbose_name='Label logo')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Short label description')),
                ('is_main', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-is_main'],
            },
        ),
    ]
