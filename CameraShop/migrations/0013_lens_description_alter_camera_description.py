# Generated by Django 4.0.4 on 2022-06-10 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CameraShop', '0012_lens_importdate_lens_isdiscount_lens_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lens',
            name='description',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='camera',
            name='description',
            field=models.CharField(max_length=1000),
        ),
    ]