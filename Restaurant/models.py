from django.db import models

from Admin.models import *
from Guest.models import *
# Create your models here.


class tbl_food(models.Model):
    food_name=models.CharField(max_length=50)
    foodtype=models.ForeignKey(tbl_foodtype,on_delete=models.CASCADE,null=True)
    category=models.ForeignKey(tbl_category,on_delete=models.CASCADE,null=True)
    rest=models.ForeignKey(tbl_restaurant,on_delete=models.CASCADE,null=True)
    food_photo=models.FileField(upload_to='Assets/FoodImage/')
    food_price=models.CharField(max_length=50)














