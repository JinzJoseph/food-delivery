# Generated by Django 5.0.4 on 2024-04-17 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0015_alter_tbl_cart_cart_qty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_booking',
            name='user',
        ),
        migrations.RemoveField(
            model_name='tbl_complaint',
            name='user',
        ),
        migrations.RemoveField(
            model_name='tbl_feedback',
            name='user',
        ),
        migrations.RemoveField(
            model_name='tbl_page',
            name='user',
        ),
    ]