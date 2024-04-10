from django.db import models
from Admin.models import *


class tbl_user(models.Model):
    user_name=models.CharField(max_length=50)
    user_gender=models.CharField(max_length=50)
    user_contact=models.CharField(max_length=50)
    user_email=models.CharField(max_length=50)
    user_password=models.CharField(max_length=50)
    place = models.ForeignKey(tbl_place, on_delete=models.CASCADE)
    

class tbl_restaurant(models.Model):
    rest_name=models.CharField(max_length=50)
    rest_contact=models.CharField(max_length=50)
    rest_email=models.CharField(max_length=50)
    rest_password=models.CharField(max_length=50)
    place = models.ForeignKey(tbl_place, on_delete=models.CASCADE)
    rest_photo = models.FileField(upload_to='Assets/ResturantPhoto/')
    rest_proof = models.FileField(upload_to='Assets/ResturantProof/')
    rest_status = models.IntegerField(default="0")

class tbl_deliveryboy(models.Model):
    dboy_name=models.CharField(max_length=50)
    dboy_gender=models.CharField(max_length=50)
    dboy_contact=models.CharField(max_length=50)
    dboy_email=models.CharField(max_length=50)
    dboy_password=models.CharField(max_length=50)
    place = models.ForeignKey(tbl_place, on_delete=models.CASCADE)
    dboy_photo = models.FileField(upload_to='Assets/DBoyPhoto/')
    dboy_proof = models.FileField(upload_to='Assets/DBoyProof/')
    dboy_status = models.IntegerField(default="0")