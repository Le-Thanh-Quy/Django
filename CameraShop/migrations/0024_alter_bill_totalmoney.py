# Generated by Django 4.0.4 on 2022-06-19 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CameraShop', '0023_alter_bill_releasetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='totalMoney',
            field=models.FloatField(null=True),
        ),
    ]
