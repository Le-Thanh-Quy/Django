# Generated by Django 4.0.4 on 2022-06-19 06:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CameraShop', '0015_camerabill_quantity_lensbill_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camerabill',
            name='paymentMethods',
            field=models.CharField(choices=[('Cash on delivery', 'Cash on delivery'), ('Debit or Credit Card', 'Debit or Credit Card'), ('PayPal', 'PayPal')], max_length=100),
        ),
        migrations.AlterField(
            model_name='lensbill',
            name='paymentMethods',
            field=models.CharField(choices=[('Cash on delivery', 'Cash on delivery'), ('Debit or Credit Card', 'Debit or Credit Card'), ('PayPal', 'PayPal')], max_length=100),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cameras', models.ManyToManyField(to='CameraShop.camera', verbose_name='list of camera')),
                ('lens', models.ManyToManyField(to='CameraShop.lens', verbose_name='list of len')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CameraShop.user')),
            ],
        ),
    ]
