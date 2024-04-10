from django.shortcuts import redirect, render

from Admin.models import *
from Guest.models import *
from Deliveryboy.models import *
from User.models import *
# Create your views here.





def Logout(request):
    del request.session['did']
    return redirect('Guest:Login')
def Myprofile(request):
    deliveryboy_data=tbl_deliveryboy.objects.get(id=request.session['did'])
    return render(request,"deliveryboy/Myprofie.html",{'Deliveryboy':deliveryboy_data})


def HomePage(request):
    if 'did' in request.session:
        id=tbl_deliveryboy.objects.get(id=request.session["did"])
        name=id.dboy_name
        return render(request,"Deliveryboy/deliveryhome.html",{"name":name})
    else:
        return redirect('Guest:login')
    

def Changepassword(request):
        if request.method=='POST':
             
            deliveryboy_data=tbl_deliveryboy.objects.get(id=request.session['did'])
            currentpswd=request.POST.get("current_pswd")
            newpswd=request.POST.get("new_pswd")
            confirmpswd=request.POST.get("confirm_pswd")
            if deliveryboy_data.password==currentpswd:
                if newpswd == confirmpswd :
                     deliveryboy_data.password=request.POST.get("new_pswd")
                     deliveryboy_data.save()
                     return render(request,'Deliveryboy/ChangePassword.html',{'Deliveryboy':deliveryboy_data})
                else:
                    msg="PASSWORD MISMATCH"
                    return render(request,'Deliveryboy/ChangePassword.html',{'msg':msg})
            else:
                msg="INVALID CURRENT PASSWORD"
                return render(request,'Deliveryboy/ChangePassword.html',{'msg':msg})
        else:
             return render(request,"Deliveryboy/ChangePassword.html")    
        

def Editprofile(request):
            deliveryboy_data=tbl_deliveryboy.objects.get(id=request.session['did'])
            if request.method=='POST':
                deliveryboy_data.dboy_name=request.POST.get("txt_name")
                deliveryboy_data.dboy_contact=request.POST.get("txt_contact")
                deliveryboy_data.dboy_email=request.POST.get("txt_email")
                deliveryboy_data.save()
                return redirect('Deliveryboy:MyProfile')
            else:
                return render(request,"Deliveryboy/Editprofile.html",{'Deliveryboy':deliveryboy_data})


def AssignedOrder(request):
    id=tbl_deliveryboy.objects.get(id=request.session["did"])
    userdata = tbl_booking.objects.filter(booking_status=4,delivery=id)
    return render(request,"Deliveryboy/AssignedOrder.html",{"userdata":userdata})