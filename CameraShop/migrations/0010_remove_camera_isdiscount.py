# Generated by Django 4.0.4 on 2022-06-09 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CameraShop', '0009_alter_camera_isdiscount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='camera',
            name='isDiscount',
        ),
    ]