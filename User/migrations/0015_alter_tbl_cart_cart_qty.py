# Generated by Django 5.0.2 on 2024-03-13 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0014_alter_tbl_booking_delivery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_cart',
            name='cart_qty',
            field=models.CharField(default=1, max_length=50),
        ),
    ]