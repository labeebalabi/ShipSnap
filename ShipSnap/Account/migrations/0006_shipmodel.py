# Generated by Django 4.2.2 on 2023-10-09 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0005_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShipModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fr_name', models.CharField(max_length=30)),
                ('fr_phone', models.IntegerField()),
                ('fr_landmark', models.CharField(max_length=30)),
                ('fr_district', models.CharField(choices=[('kasarkode', 'kasarkode'), ('kannur', 'kannur'), ('kozhikode', 'kozhikode'), ('malappuram', 'malappuram'), ('wayanad', 'wayanad'), ('palakkad', 'palakkad'), ('idukki', 'idukki'), ('thrissur', 'thrissur'), ('eranakulam', 'eranakulam'), ('alappuzha', 'alappuzha'), ('pathanamthitta', 'pathanamthitta'), ('kollam', 'kollam'), ('kottayam', 'kottayam'), ('thiruvananthapuram', 'thiruvananthapuram')], default='kannur', max_length=100)),
                ('fr_addrss', models.TextField(max_length=300)),
                ('to_name', models.CharField(max_length=30)),
                ('to_phone', models.IntegerField()),
                ('to_landmark', models.CharField(max_length=30)),
                ('to_district', models.CharField(choices=[('kasarkode', 'kasarkode'), ('kannur', 'kannur'), ('kozhikode', 'kozhikode'), ('malappuram', 'malappuram'), ('wayanad', 'wayanad'), ('palakkad', 'palakkad'), ('idukki', 'idukki'), ('thrissur', 'thrissur'), ('eranakulam', 'eranakulam'), ('alappuzha', 'alappuzha'), ('pathanamthitta', 'pathanamthitta'), ('kollam', 'kollam'), ('kottayam', 'kottayam'), ('thiruvananthapuram', 'thiruvananthapuram')], default='kannur', max_length=100)),
                ('to_addrss', models.TextField(max_length=300)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Account.product')),
            ],
        ),
    ]
