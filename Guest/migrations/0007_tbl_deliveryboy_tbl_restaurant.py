# Generated by Django 5.0.2 on 2024-03-07 10:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0003_tbl_admin'),
        ('Guest', '0006_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_deliveryboy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dboy_name', models.CharField(max_length=50)),
                ('dboy_gender', models.CharField(max_length=50)),
                ('dboy_contact', models.CharField(max_length=50)),
                ('dboy_email', models.CharField(max_length=50)),
                ('dboy_password', models.CharField(max_length=50)),
                ('dboy_photo', models.FileField(upload_to='Assets/DBoyPhoto/')),
                ('dboy_proof', models.FileField(upload_to='Assets/DBoyProof/')),
                ('dboy_status', models.IntegerField(default='0')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_place')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rest_name', models.CharField(max_length=50)),
                ('rest_gender', models.CharField(max_length=50)),
                ('rest_contact', models.CharField(max_length=50)),
                ('rest_email', models.CharField(max_length=50)),
                ('rest_password', models.CharField(max_length=50)),
                ('rest_photo', models.FileField(upload_to='Assets/ResturantPhoto/')),
                ('rest_proof', models.FileField(upload_to='Assets/ResturantProof/')),
                ('rest_status', models.IntegerField(default='0')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_place')),
            ],
        ),
    ]