# Generated by Django 4.0.4 on 2022-06-19 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CameraShop', '0021_bill_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='instructions',
            field=models.CharField(max_length=1500, null=True),
        ),
    ]