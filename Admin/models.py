from django.db import models


# Create your models here.

class tbl_admin(models.Model):
    admin_name=models.CharField(max_length=50)
    admin_contact=models.CharField(max_length=50)
    admin_email=models.CharField(max_length=50)
    admin_password=models.CharField(max_length=50)




class tbl_district(models.Model):
    district_name=models.CharField(max_length=50)

class tbl_category(models.Model):
    category_name=models.CharField(max_length=50)


class tbl_complainttype(models.Model):
    complaint_type=models.CharField(max_length=50)

class tbl_place(models.Model):
    place_name=models.CharField(max_length=50)
    place_pincode=models.IntegerField(null=True)
    district=models.ForeignKey(tbl_district,on_delete=models.CASCADE,null=True)


class tbl_foodtype(models.Model):
    foodtype_name=models.CharField(max_length=50)