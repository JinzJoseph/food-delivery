from django.db import models
from Guest.models import *
from Restaurant.models import *
# Create your models here.



class tbl_post(models.Model):
    post_caption=models.CharField(max_length=50)
    post_description=models.CharField(max_length=200)
    post_photo=models.FileField(upload_to='Food/')



class tbl_complaint(models.Model):
    complaint_title=models.CharField(max_length=500)
    complaint_details=models.CharField(max_length=500)
    complaint_postdate=models.DateField(auto_now_add=True)
    complaint_reply=models.CharField(max_length=500)
    complaint_replydate=models.DateField(null=True)
    complaint_status = models.IntegerField(default="0")
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE,null=True)
    

class tbl_feedback(models.Model):
    feedback_subject=models.CharField(max_length=500)
    feedback_details=models.CharField(max_length=500)
    feedback_postdate=models.DateField(auto_now_add=True)
    feedback_status = models.IntegerField(default="0")
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE)
    

class tbl_page(models.Model):
    page_name=models.CharField(max_length=500)
    page_bio=models.CharField(max_length=500)
    page_doj=models.DateField(auto_now_add=True)
    page_photo = models.FileField(upload_to='Assets/PagePhoto/')
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE)

class tbl_booking(models.Model):
    booking_amount=models.CharField(max_length=50)
    booking_datetime=models.DateTimeField(auto_now_add=True)
    booking_status = models.IntegerField(default="0")
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE)
    delivery = models.ForeignKey(tbl_deliveryboy, on_delete=models.CASCADE, null=True)

class tbl_cart(models.Model):
    cart_qty=models.CharField(max_length=50,default=1)
    cart_status = models.IntegerField(default="0")
    food = models.ForeignKey(tbl_food, on_delete=models.CASCADE)
    booking = models.ForeignKey(tbl_booking, on_delete=models.CASCADE)