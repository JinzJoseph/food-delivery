# Generated by Django 5.0.4 on 2024-04-17 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0008_remove_tbl_restaurant_rest_gender_and_more'),
        ('User', '0016_remove_tbl_booking_user_remove_tbl_complaint_user_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tbl_user',
        ),
    ]