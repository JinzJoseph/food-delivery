# Generated by Django 5.0.4 on 2024-04-17 08:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Guest', '0010_tbl_user'),
        ('Restaurant', '0003_initial'),
        ('User', '0017_remove_tbl_booking_delivery_remove_tbl_cart_booking_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_caption', models.CharField(max_length=50)),
                ('post_description', models.CharField(max_length=200)),
                ('post_photo', models.FileField(upload_to='Food/')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_amount', models.CharField(max_length=50)),
                ('booking_datetime', models.DateTimeField(auto_now_add=True)),
                ('booking_status', models.IntegerField(default='0')),
                ('delivery', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_deliveryboy')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_qty', models.CharField(default=1, max_length=50)),
                ('cart_status', models.IntegerField(default='0')),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.tbl_booking')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Restaurant.tbl_food')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint_title', models.CharField(max_length=500)),
                ('complaint_details', models.CharField(max_length=500)),
                ('complaint_postdate', models.DateField(auto_now_add=True)),
                ('complaint_reply', models.CharField(max_length=500)),
                ('complaint_replydate', models.DateField(null=True)),
                ('complaint_status', models.IntegerField(default='0')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_subject', models.CharField(max_length=500)),
                ('feedback_details', models.CharField(max_length=500)),
                ('feedback_postdate', models.DateField(auto_now_add=True)),
                ('feedback_status', models.IntegerField(default='0')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_name', models.CharField(max_length=500)),
                ('page_bio', models.CharField(max_length=500)),
                ('page_doj', models.DateField(auto_now_add=True)),
                ('page_photo', models.FileField(upload_to='Assets/PagePhoto/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user')),
            ],
        ),
    ]