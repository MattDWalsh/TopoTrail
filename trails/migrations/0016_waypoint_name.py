# Generated by Django 4.0.4 on 2022-06-03 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trails', '0015_trail_status_heightmap_trail_status_mesh_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='waypoint',
            name='name',
            field=models.CharField(default='name', max_length=50),
            preserve_default=False,
        ),
    ]
