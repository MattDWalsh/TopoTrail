# Generated by Django 4.0.4 on 2022-06-22 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trails', '0015_alter_photo_photo_alter_trailtype_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trailtype',
            name='type',
            field=models.CharField(choices=[('cycling', 'Cycling'), ('hiking', 'Hiking'), ('climbing', 'Climbing')], max_length=50),
        ),
    ]
