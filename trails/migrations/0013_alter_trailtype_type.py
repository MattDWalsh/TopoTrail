# Generated by Django 4.0.4 on 2022-06-22 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trails', '0012_alter_photo_thumb_alter_trailtype_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trailtype',
            name='type',
            field=models.CharField(choices=[('cycling', 'Cycling'), ('climbing', 'Climbing'), ('hiking', 'Hiking')], max_length=50),
        ),
    ]
