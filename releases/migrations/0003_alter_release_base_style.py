# Generated by Django 3.2.4 on 2021-07-30 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('releases', '0002_auto_20210730_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='release',
            name='base_style',
            field=models.CharField(choices=[('BM', 'Black Metal'), ('DM', 'Death Metal'), ('TM', 'Thrash Metal')], max_length=250),
        ),
    ]
