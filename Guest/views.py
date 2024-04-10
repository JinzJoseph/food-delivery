from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
# Create your views here.


def LoadMainIndex(request):
    return render(request,"Guest/Index.html")

def userRegistration(request):
    district = tbl_district.objects.all()
    if request.method=="POST":
        place = tbl_place.objects.get(id=request.POST.get('sel_place'))
        tbl_user.objects.create(user_name=request.POST.get("txtname"),user_gender=request.POST.get("gender"),user_contact=request.POST.get("txtcontact"),user_email=request.POST.get("txtemail"),user_password=request.POST.get("txtpwd"),place=place)
        return redirect("Guest:userRegistration")
    else:
        return render(request,"Guest/NewUser.html",{"districtdata":district})
    
def ResturantRegistration(request):
    district = tbl_district.objects.all()
    if request.method=="POST":
        place = tbl_place.objects.get(id=request.POST.get('sel_place'))
        tbl_restaurant.objects.create(rest_name=request.POST.get("txtname"),rest_contact=request.POST.get("txtcontact"),rest_email=request.POST.get("txtemail"),rest_photo=request.FILES.get("fileImage"),rest_proof=request.FILES.get("fileProof"),rest_password=request.POST.get("txtpwd"),place=place)
        return redirect("Guest:ResturantRegistration")
    else:
        return render(request,"Guest/NewResturant.html",{"districtdata":district})

def DliveryBoyRegistration(request):
    district = tbl_district.objects.all()
    if request.method=="POST":
        place = tbl_place.objects.get(id=request.POST.get('sel_place'))
        tbl_deliveryboy.objects.create(dboy_name=request.POST.get("txtname"),dboy_gender=request.POST.get("gender"),dboy_contact=request.POST.get("txtcontact"),dboy_email=request.POST.get("txtemail"),dboy_photo=request.FILES.get("fileImage"),dboy_proof=request.FILES.get("fileProof"),dboy_password=request.POST.get("txtpwd"),place=place)
        return redirect("Guest:DliveryBoyRegistration")
    else:
        return render(request,"Guest/NewDliveryBoy.html",{"districtdata":district})
       
def ajaxplace(request):
    dis = tbl_district.objects.get(id=request.GET.get("did"))
    place = tbl_place.objects.filter(district=dis)
    return render(request,"Guest/AjaxPlace.html",{"placedata":place})


def Login(request):
    if request.method == "POST":
        admincount = tbl_admin.objects.filter(admin_email=request.POST.get("txt_email"),admin_password=request.POST.get("txt_password")).count()
        usercount = tbl_user.objects.filter(user_email=request.POST.get("txt_email"),user_password=request.POST.get("txt_password")).count()
        restcount = tbl_restaurant.objects.filter(rest_status='1',rest_email=request.POST.get("txt_email"),rest_password=request.POST.get("txt_password")).count()
        dboycount = tbl_deliveryboy.objects.filter(dboy_status='1',dboy_email=request.POST.get("txt_email"),dboy_password=request.POST.get("txt_password")).count()
        

        if admincount > 0:
            user = tbl_admin.objects.get(admin_email=request.POST.get("txt_email"),admin_password=request.POST.get("txt_password"))
            request.session["adminid"] = user.id
            request.session["adminname"] = user.admin_name
            return redirect("Admin:LoadingHomePage")
        elif usercount > 0:
            user = tbl_user.objects.get(user_email=request.POST.get("txt_email"),user_password=request.POST.get("txt_password"))
            request.session["uid"] = user.id
            request.session["uname"] = user.user_name
            return redirect("User:Userhome")
        elif restcount > 0:
            user = tbl_restaurant.objects.get(rest_email=request.POST.get("txt_email"),rest_password=request.POST.get("txt_password"))
            request.session["rid"] = user.id
            request.session["tname"] = user.rest_name
            return redirect("Restaurant:HomePage")
        elif dboycount > 0:
            user = tbl_deliveryboy.objects.get(dboy_email=request.POST.get("txt_email"),dboy_password=request.POST.get("txt_password"))
            request.session["did"] = user.id
            request.session["dname"] = user.dboy_name
            return redirect("Deliveryboy:HomePage")
        else:
            return render(request,"Guest/Login.html",{"msg":"Invalid Email Or Password"})
    else:
        return render(request,"Guest/Login.html")