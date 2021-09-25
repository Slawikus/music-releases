# Generated by Django 3.2.7 on 2021-09-24 15:17

import configuration.file_storage
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import releases.models.release


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('releases', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='release',
            name='base_style',
            field=models.CharField(blank=True, choices=[('black_metal', 'Black Metal'), ('death_metal', 'Death Metal'), ('trash_metal', 'Thrash Metal')], max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='release',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True, verbose_name='Band country'),
        ),
        migrations.AlterField(
            model_name='release',
            name='cover_image',
            field=models.ImageField(blank=True, help_text='Select image with minimum size of 800x800 pixel', null=True, storage=configuration.file_storage.DuplicationFixFileSystemStorage(), upload_to='images/covers/', verbose_name='Front cover image'),
        ),
        migrations.AlterField(
            model_name='release',
            name='format',
            field=models.CharField(blank=True, choices=[('CD', 'CD'), ('Vinyl', 'Vinyl'), ('Tape', 'Tape'), ('DVD', 'DVD')], default='CD', max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='release',
            name='label',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='releases', to='users.label'),
        ),
        migrations.AlterField(
            model_name='release',
            name='release_date',
            field=models.DateField(blank=True, help_text='For past/old releases exact date is not important, feel free just to select January 1st, but with correct year. For recent/upcoming releases - please try to set the date exactly. This release will be shown in Upcoming Releases section.', null=True, verbose_name='Release date'),
        ),
        migrations.AlterField(
            model_name='release',
            name='sample',
            field=models.FileField(blank=True, help_text='Upload up to 1 minute sample of the album to give fellow label owners a taste of this release', null=True, storage=configuration.file_storage.DuplicationFixFileSystemStorage(), upload_to='audios/releases/', validators=[releases.models.release.validate_file_size, django.core.validators.FileExtensionValidator(['mp3'])]),
        ),
    ]
