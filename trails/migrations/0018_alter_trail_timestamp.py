# Generated by Django 4.0.4 on 2022-06-03 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trails', '0017_trail_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trail',
            name='timestamp',
            field=models.DateTimeField(),
        ),
    ]
