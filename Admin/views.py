from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
# Create your views here.
from User.models import *
from datetime import date
from django.views import View



def LoadingHomePage(request):
    return render(request,"Admin/HomePage.html")
def logout(request):
    del request.session['adminid']
    return redirect('Guest:Login')

def District(request):
    district=tbl_district.objects.all()
    if request.method=="POST":
       tbl_district.objects.create(district_name=request.POST.get("District"))
       return render(request,"Admin/District.html",{'districtdata':district})
    else:
        return render(request,"Admin/District.html",{'districtdata':district})

def DeleteDistrict(request,did):
    tbl_district.objects.get(id=did).delete()
    return redirect("Admin:District")

def EditDistrict(request,eid):
    disdata=tbl_district.objects.get(id=eid)
    if request.method=="POST":
        disdata.district_name=request.POST.get('District')
        disdata.save()
        return redirect("Admin:District")
    else:
        return render(request,"Admin/District.html",{'disdata':disdata})



def Place(request):
    disob=tbl_district.objects.all()
    Place=tbl_place.objects.all()
    if request.method=="POST":
        dis=tbl_district.objects.get(id=request.POST.get('sel_district'))
        tbl_place.objects.create(
            place_name=request.POST.get("place"),
            place_pincode=request.POST.get('pincode'),
            district=dis)
        return render(request,"Admin/place.html",{'placedata':Place,'disob':disob})
    else:
        return render(request,"Admin/place.html",{'placedata':Place,'disob':disob})


def DeletePlace(request,did):
    tbl_place.objects.get(id=did).delete()
    return redirect("Admin:Place")





def Category(request):
    category=tbl_category.objects.all()
    if request.method=="POST":
       tbl_category.objects.create(category_name=request.POST.get("Category"))
       return render(request,"Admin/Category.html",{'categorydata':category})
    else:
        return render(request,"Admin/Category.html",{'categorydata':category})

def DeleteCategory(request,did):
    tbl_category.objects.get(id=did).delete()
    return redirect("Admin:Category")

def EditCategory(request,eid):
    catdata=tbl_category.objects.get(id=eid)
    if request.method=="POST":
        catdata.category_name=request.POST.get('Category')
        catdata.save()
        return redirect("Admin:Category")
    else:
        return render(request,"Admin/Category.html",{'catdata':catdata})
    






def Complainttype(request):
    complainttype=tbl_complainttype.objects.all()
    if request.method=="POST":
        tbl_complainttype.objects.create(complaint_type=request.POST.get("complainttype"))
        return render(request,"Admin/Complainttype.html",{'complaintdata':complainttype})
    else:
        return render(request,"Admin/Complainttype.html",{'complaintdata':complainttype})
def DeleteComplainttype(request,did):
    tbl_complainttype.objects.get(id=did).delete()
    return redirect("Admin:Complainttype")

def Editcomplainttype(request,eid):
    comdata=tbl_complainttype.objects.get(id=eid)
    if request.method=="POST":
        comdata.complaint_type=request.POST.get("complainttype")
        comdata.save()
        return redirect("Admin:Complainttype")
    else:
        return render(request,"Admin/Complainttype.html",{'comdata':comdata})





def Foodtype(request):
    foodtype=tbl_foodtype.objects.all()
    if request.method=="POST":
       tbl_foodtype.objects.create(foodtype_name=request.POST.get("foodtype"))
       return render(request,"Admin/Foodtype.html",{'districtdata':foodtype})
    else:
        return render(request,"Admin/Foodtype.html",{'districtdata':foodtype})

def DeleteFoodtype(request,did):
    tbl_foodtype.objects.get(id=did).delete()
    return redirect("Admin:Foodtype")

def EditFoodtype(request,eid):
    disdata=tbl_foodtype.objects.get(id=eid)
    if request.method=="POST":
        disdata.foodtype_name=request.POST.get('foodtype')
        disdata.save()
        return redirect("Admin:Foodtype")
    else:
        return render(request,"Admin/Foodtype.html",{'disdata':disdata})


def adminInsertSelect(request):
    data=tbl_admin.objects.all()
    if request.method=="POST":
        name=request.POST.get('txtname')
        contact=request.POST.get('txtcontact')
        email=request.POST.get('txtemail')
        pwd=request.POST.get('txtpwd')
        tbl_admin.objects.create(admin_name=name,admin_contact=contact,admin_email=email,admin_password=pwd)
        return redirect("Admin:adminInsertSelect")
    else:
        return render(request,"Admin/AdminRegistration.html",{'data':data})

def delAdminReg(request,did):
    tbl_admin.objects.get(id=did).delete()
    return redirect("Admin:adminInsertSelect")

def adminRegUpdate(request,eid):
    editdata=tbl_admin.objects.get(id=eid)
    if request.method=="POST":
        editdata.admin_name=request.POST.get("txtname")
        editdata.admin_contact=request.POST.get("txtcontact")
        editdata.admin_email=request.POST.get("txtemail")
        editdata.admin_password=request.POST.get("txtpwd")
        editdata.save()
        return redirect("Admin:adminInsertSelect")
    else:
        return render(request,"Admin\AdminRegistration.html",{"editdata":editdata})
    


def userListNew(request):
    userdata = tbl_user.objects.all()
    return render(request,"Admin/UserListNew.html",{"userdata":userdata})


def ResturantListNew(request):
    userdata = tbl_restaurant.objects.filter(rest_status=0)
    return render(request,"Admin/ResturantListNew.html",{"userdata":userdata})

def acceptresturant(request,aid):
    user = tbl_restaurant.objects.get(id=aid)
    user.rest_status = 1
    user.save()
    return redirect("Admin:LoadingHomePage")

def rejectresturant(request,rid):
    user = tbl_restaurant.objects.get(id=rid)
    user.rest_status = 2
    user.save()
    return redirect("Admin:LoadingHomePage")

def ResturantListAccepted(request):
    userdata = tbl_restaurant.objects.filter(rest_status=1)
    return render(request,"Admin/ResturantListAccepted.html",{"userdata":userdata})

def ResturantListRejected(request):
    userdata = tbl_restaurant.objects.filter(rest_status=2)
    return render(request,"Admin/ResturantListRejected.html",{"userdata":userdata})



def DeliveryBoyListNew(request):
    userdata = tbl_deliveryboy.objects.filter(dboy_status=0)
    return render(request,"Admin/DeliveryBoyListNew.html",{"userdata":userdata})

def acceptdeliveryboy(request,aid):
    user = tbl_deliveryboy.objects.get(id=aid)
    user.dboy_status = 1
    user.save()
    return redirect("Admin:LoadingHomePage")

def rejectdeliveryboy(request,rid):
    user = tbl_deliveryboy.objects.get(id=rid)
    user.dboy_status = 2
    user.save()
    return redirect("Admin:LoadingHomePage")

def DeliveryBoyListAccepted(request):
    userdata = tbl_deliveryboy.objects.filter(dboy_status=1)
    return render(request,"Admin/DeliveryBoyListAccepted.html",{"userdata":userdata})

def DeliveryBoyListRejected(request):
    userdata = tbl_deliveryboy.objects.filter(dboy_status=2)
    return render(request,"Admin/DeliveryBoyListRejected.html",{"userdata":userdata})



def ComplaintListNew(request):
    userdata=tbl_user.objects.all()
    userComplaint=tbl_complaint.objects.filter(complaint_status=0,user__in=userdata)
    return render(request,"Admin/ComplaintListNew.html",{'userComplaint':userComplaint})

def ComplaintReply(request,cid):
    complaint = tbl_complaint.objects.get(id=cid)
    if request.method=="POST":
        complaint.complaint_replydate = date.today()
        complaint.complaint_reply=request.POST.get('txtreply')
        complaint.complaint_status=1
        complaint.save()
        return redirect("Admin:LoadingHomePage")
    else:
        return render(request,"Admin/ComplaintListReply.html",{'complaint':complaint})
    
def ComplaintSolved(request):
    userdata=tbl_user.objects.all()
    userComplaint=tbl_complaint.objects.filter(complaint_status=1,user__in=userdata)
   
    return render(request,"Admin/ComplaintListSolved.html",{'userComplaint':userComplaint})
    

def UserFeedbackNew(request):
    data=tbl_feedback.objects.filter(feedback_status=0)
    return render(request,"Admin/UserFeedBack.html",{'data':data})

# def report(request):
#     if request.method=="POST":
#         data=tbl_booking.objects.all()
#         return render(request,"Admin/Report.html",{'data':data})   
#     else:
#         return render(request,"Admin/Report.html")
def viewbooking(request):
      restaurant_data=tbl_restaurant.objects.all()
      booking_ids = tbl_cart.objects.filter(food__rest__in=restaurant_data).values_list('booking_id', flat=True)
      bookings = tbl_booking.objects.filter(id__in=booking_ids, booking_status='3')
      print(bookings)
      return render(request,"Admin/Report.html",{'data':bookings})


