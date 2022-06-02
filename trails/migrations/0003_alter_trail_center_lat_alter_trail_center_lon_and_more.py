# Generated by Django 4.0.4 on 2022-06-01 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trails', '0002_trail_share'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trail',
            name='center_lat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='trail',
            name='center_lon',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='trail',
            name='mesh',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='trail',
            name='share',
            field=models.CharField(choices=[('private', 'Private'), ('public', 'Public'), ('link', 'Link')], default='private', max_length=7),
        ),
        migrations.AlterField(
            model_name='trail',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='trail',
            name='texture_sat',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='trail',
            name='texture_trail',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
