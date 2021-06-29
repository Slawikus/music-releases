# Generated by Django 3.2 on 2021-06-18 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_profile_label_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='currencies',
            field=models.CharField(blank=True, choices=[('USD', 'American Dollar'), ('EUR', 'Euro'), ('UAH', 'Ukrainian Hrivna')], default='usd', max_length=15, null=True),
        ),
    ]
