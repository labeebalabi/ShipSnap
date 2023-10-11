# Generated by Django 4.2.2 on 2023-10-09 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0003_product_kilo_meter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='kilo_meter',
            field=models.IntegerField(verbose_name='Distance in Kilometer'),
        ),
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.FloatField(verbose_name='Product Weight'),
        ),
    ]