# Generated by Django 4.2.2 on 2023-10-10 16:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Account', '0008_alter_shipmodel_fr_district_alter_shipmodel_fr_phone_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='save',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Account.shipmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Status', models.CharField(choices=[('Confirmed', 'Confirmed'), ('Shipped', 'Shipped'), ('Order cancelled', 'Order cancelled')], default='Confirmed', max_length=200)),
                ('ship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Account.shipmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
