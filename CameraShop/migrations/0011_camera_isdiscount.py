# Generated by Django 4.0.4 on 2022-06-09 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CameraShop', '0010_remove_camera_isdiscount'),
    ]

    operations = [
        migrations.AddField(
            model_name='camera',
            name='isDiscount',
            field=models.BooleanField(default=False),
        ),
    ]