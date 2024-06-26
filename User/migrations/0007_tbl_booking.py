# Generated by Django 5.0.2 on 2024-03-09 10:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0003_initial'),
        ('User', '0006_tbl_page'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_qty', models.CharField(max_length=50)),
                ('cart_status', models.IntegerField(default='0')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Restaurant.tbl_food')),
            ],
        ),
    ]
