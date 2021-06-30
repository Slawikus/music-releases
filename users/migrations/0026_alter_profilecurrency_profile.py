# Generated by Django 3.2 on 2021-06-27 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0025_alter_profilecurrency_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilecurrency',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='currencies', to='users.profile', unique=True),
        ),
    ]
