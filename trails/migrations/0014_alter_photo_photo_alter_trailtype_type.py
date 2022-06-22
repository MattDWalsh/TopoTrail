# Generated by Django 4.0.4 on 2022-06-22 17:23

from django.db import migrations, models
import trails.models


class Migration(migrations.Migration):

    dependencies = [
        ('trails', '0013_alter_trailtype_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(blank=True, max_length=512, null=True, upload_to=trails.models.photo_location),
        ),
        migrations.AlterField(
            model_name='trailtype',
            name='type',
            field=models.CharField(choices=[('climbing', 'Climbing'), ('hiking', 'Hiking'), ('cycling', 'Cycling')], max_length=50),
        ),
    ]
