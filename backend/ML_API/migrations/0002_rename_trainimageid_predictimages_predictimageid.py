# Generated by Django 4.1.7 on 2023-03-05 02:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ML_API', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='predictimages',
            old_name='TrainImageId',
            new_name='PredictImageId',
        ),
    ]