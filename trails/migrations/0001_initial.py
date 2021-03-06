# Generated by Django 4.0.4 on 2022-06-04 02:26

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import trails.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Trail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.CharField(blank=True, max_length=500, null=True)),
                ('trail_file', models.FileField(upload_to=trails.models.trail_file_location, validators=[django.core.validators.FileExtensionValidator(['geojson', 'gpx'])])),
                ('share', models.CharField(choices=[('private', 'Private'), ('public', 'Public'), ('link', 'Link')], default='private', max_length=7)),
                ('timestamp', models.DateTimeField()),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('min_lat', models.FloatField(blank=True, null=True)),
                ('max_lat', models.FloatField(blank=True, null=True)),
                ('min_lon', models.FloatField(blank=True, null=True)),
                ('max_lon', models.FloatField(blank=True, null=True)),
                ('center_lat', models.FloatField(blank=True, null=True)),
                ('center_lon', models.FloatField(blank=True, null=True)),
                ('heightmap', models.FileField(blank=True, null=True, upload_to=trails.models.heightmap_location)),
                ('mesh', models.FileField(blank=True, null=True, upload_to=trails.models.mesh_location)),
                ('texture_sat', models.ImageField(blank=True, null=True, upload_to=trails.models.texture_sat_location)),
                ('texture_trail', models.ImageField(blank=True, null=True, upload_to=trails.models.texture_trail_location)),
                ('status_parsed', models.FloatField(default=0)),
                ('status_waypoints', models.FloatField(default=0)),
                ('status_heightmap', models.FloatField(default=0)),
                ('status_mesh', models.FloatField(default=0)),
                ('status_texture_trail', models.FloatField(default=0)),
                ('status_texture_satellite', models.FloatField(default=0)),
                ('status_overall', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Waypoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('position', models.IntegerField()),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('notes', models.CharField(blank=True, max_length=200, null=True)),
                ('parent_trail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trails.trail')),
            ],
        ),
    ]
