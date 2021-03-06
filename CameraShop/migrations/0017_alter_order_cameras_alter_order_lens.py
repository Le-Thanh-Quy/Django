# Generated by Django 4.0.4 on 2022-06-19 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CameraShop', '0016_alter_camerabill_paymentmethods_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cameras',
            field=models.ManyToManyField(null=True, to='CameraShop.camera', verbose_name='list of camera'),
        ),
        migrations.AlterField(
            model_name='order',
            name='lens',
            field=models.ManyToManyField(null=True, to='CameraShop.lens', verbose_name='list of len'),
        ),
    ]
