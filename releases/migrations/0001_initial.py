# Generated by Django 3.2.4 on 2021-07-29 11:36

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import releases.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Release',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('band_name', models.CharField(help_text='Enter band name here. If split release - add band names with“/“ i.e. Nokturnal Mortum / Drudkh', max_length=250, verbose_name='Band name(s)')),
                ('country', django_countries.fields.CountryField(max_length=2, verbose_name='Band country')),
                ('album_title', models.CharField(max_length=250, verbose_name='Album title')),
                ('release_date', models.DateField(help_text='For past/old releases exact date is not important, feel free just to select January 1st, but with correct year. For recent/upcoming releases - please try to set the date exactly. This release will be shown in Upcoming Releases section.', verbose_name='Release date')),
                ('base_style', models.CharField(choices=[('black_Metal', 'Black Metal'), ('death_Metal', 'Death Metal'), ('thrash_Metal', 'Thrash Metal')], max_length=250)),
                ('cover_image', models.ImageField(help_text='Select image with minimum size of 800x800 pixel', upload_to='images/covers/', verbose_name='Front cover image')),
                ('format', models.CharField(choices=[('CD', 'CD'), ('Vinyl', 'Vinyl'), ('Tape', 'Tape'), ('DVD', 'DVD')], default='CD', max_length=5)),
                ('sample', models.FileField(help_text='Upload up to 1 minute sample of the album to give fellow label owners a taste of this release', upload_to='audios/releases/', validators=[releases.models.validate_file_size, django.core.validators.FileExtensionValidator(['pdf'])])),
                ('media_format_details', models.CharField(blank=True, help_text='E.g. Digipak, 2xGatefold etc.', max_length=250, null=True)),
                ('limited_edition', models.PositiveIntegerField(blank=True, null=True)),
                ('label', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='release', to='users.label')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='release', to='users.profile')),
            ],
        ),
    ]