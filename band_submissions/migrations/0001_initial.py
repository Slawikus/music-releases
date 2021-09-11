# Generated by Django 3.2.7 on 2021-09-11 12:28

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BandSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('album', models.FileField(help_text='upload zip or rar file containing your album samples', upload_to='band_submissions/files/', validators=[django.core.validators.FileExtensionValidator(['zip', 'rar'])])),
                ('best_track', models.FileField(upload_to='band_submissions/audio/', validators=[django.core.validators.FileExtensionValidator(['mp3'])], verbose_name='best track')),
                ('front_cover', models.ImageField(blank=True, null=True, upload_to='band_submissions/image/', verbose_name='front cover')),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('biography', models.TextField(help_text='Write about releases, press mention or tour dates')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to='users.profile')),
            ],
        ),
    ]
