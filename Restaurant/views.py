from django.shortcuts import redirect, render

from Admin.models import *
from Guest.models import *
from User.models import *
from Restaurant.models import *
from User.models import tbl_cart

# Create your views here.


def Logout(request):
    del request.session['rid']
    return redirect('Guest:Login')

def Myprofile(request):
    restaurant_data=tbl_restaurant.objects.get(id=request.session['rid'])
    return render(request,"Restaurant/Myprofile.html",{'restaurant':restaurant_data})


def home(request):
    if 'rid' in request.session:
        
        return render(request,"Restaurant/Home.html")
    else:
        return redirect('Guest:login')
    

def Changepassword(request):
        if request.method=='POST':
             
            restaurant_data=tbl_restaurant.objects.get(id=request.session['rid'])
            currentpswd=request.POST.get("current_pswd")
            newpswd=request.POST.get("new_pswd")
            confirmpswd=request.POST.get("confirm_pswd")
            if restaurant_data.rest_password==currentpswd:
                if newpswd == confirmpswd :
                     restaurant_data.rest_password=request.POST.get("new_pswd")
                     restaurant_data.save()
                     return render(request,'Restaurant/ChangePassword.html',{'restaurant':restaurant_data})
                else:
                    msg="PASSWORD MISMATCH"
                    return render(request,'Restaurant/ChangePassword.html',{'msg':msg})
            else:
                msg="INVALID CURRENT PASSWORD"
                return render(request,'Restaurant/ChangePassword.html',{'msg':msg})
        else:
             return render(request,"Restaurant/ChangePassword.html")    
        

def Editprofile(request):
            restaurant_data=tbl_restaurant.objects.get(id=request.session['rid'])
            if request.method=='POST':
                restaurant_data.rest_name=request.POST.get("txt_name")
                restaurant_data.rest_contact=request.POST.get("txt_contact")
                restaurant_data.rest_email=request.POST.get("txt_email")
                restaurant_data.save()
                return redirect('Restaurant:MyProfile')
            else:
                return render(request,"Restaurant/EditProfile.html",{'restaurant':restaurant_data})


def FoodInsertSelect(request):
    food=tbl_food.objects.filter(rest=request.session["rid"])
    foodType=tbl_foodtype.objects.all()
    category=tbl_category.objects.all()
    restID=tbl_restaurant.objects.get(id=request.session["rid"])
    if request.method=="POST":
       foodType=tbl_foodtype.objects.get(id=request.POST.get('sel_type'))
       category=tbl_category.objects.get(id=request.POST.get('sel_category'))
       tbl_food.objects.create(food_name=request.POST.get("food_name"),food_photo=request.FILES.get("txtphoto"),food_price=request.POST.get("price"),
       category=category,foodtype=foodType,rest=restID)
       return redirect("Restaurant:FoodInsertSelect")
    else:
        return render(request,"Restaurant/Food.html",{'fooddata':food,'foodType':foodType,'category':category})

def delFood(request,did):
    tbl_food.objects.get(id=did).delete()
    return redirect("Restaurant:FoodInsertSelect")


def viewbooking(request):
      restaurant_data=tbl_restaurant.objects.get(id=request.session['rid'])
      booking=tbl_cart.objects.filter(food__rest=restaurant_data)
      bk_id = []
      for i in booking:
        bk_id.append(i.booking_id)
    #   print(bk_id)
      book = tbl_booking.objects.filter(id__in=bk_id,booking_status='3')
      return render(request,"Restaurant/Viewbooking.html",{'data':book})


def viewproduct(request,id):
     cart = tbl_cart.objects.filter(booking=id)
     return render(request,"Restaurant/View_product.html",{"data":cart})


def AssignNowDeliveryBoy(request,did):
    dBoy=tbl_deliveryboy.objects.filter(dboy_status='1')
    bookingdata=tbl_booking.objects.get(id=did)
    if request.method=='POST':
        boy=tbl_deliveryboy.objects.get(id=request.POST.get('selBoy'))
        bookingdata.delivery=boy
        bookingdata.booking_status=4
        bookingdata.save()
        return redirect("Restaurant:HomePage")
        
    else:
         return render(request,"Restaurant/AssignNowDeliveryBoy.html",{'bookingdata':bookingdata,'dboy':dBoy})