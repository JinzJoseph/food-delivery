from xml.dom import UserDataHandler
from django.shortcuts import redirect, render
from Guest.models import  *
from User.models import *
from Admin.models import *
from Restaurant.models import *

# Create your views here.

def user_home(request):
    if 'uid' in request.session:
        
        return render(request,"User/Userhome.html")
    else:
        return redirect('Guest:login')

def changepassword(request):
        if request.method=='POST':
             
            user_data=tbl_user.objects.get(id=request.session['uid'])
            currentpswd=request.POST.get("current_pswd")
            newpswd=request.POST.get("new_pswd")
            confirmpswd=request.POST.get("confirm_pswd")
            if user_data.user_password==currentpswd:
                if newpswd == confirmpswd :
                     user_data.user_password=request.POST.get("new_pswd")
                     user_data.save()
                     return render(request,'User/ChangePassword.html',{'udata':user_data})
                else:
                    msg="PASSWORD MISMATCH"
                    return render(request,'User/ChangePassword.html',{'msg':msg})
            else:
                msg="INVALID CURRENT PASSWORD"
                return render(request,'User/ChangePassword.html',{'msg':msg})
        else:
             return render(request,"User/ChangePassword.html")   

def Myprofile(request):
    user_data=tbl_user.objects.get(id=request.session['uid'])
    return render(request,"User/Myprofile.html",{'user':user_data})





def Editprofile(request):
            user_data=tbl_user.objects.get(id=request.session['uid'])
            if request.method=='POST':
                user_data.user_name=request.POST.get("txt_name")
                user_data.user_contact=request.POST.get("txt_contact")
                user_data.user_Email=request.POST.get("txt_email")
                user_data.user_address=request.POST.get("txt_address")
                user_data.save()
                return redirect('User:Myprofile')
            else:
                return render(request,"User/EditProfile.html",{'user':user_data})


def Post(request):
    post=tbl_post.objects.all()
    if request.method=="POST":
       tbl_post.objects.create(post_caption=request.POST.get("post_caption"),post_description=request.POST.get("post_description"),post_photo=request.FILES.get("txtphoto")) 
       return render(request,"User/Post.html",{'postdata':post})
    else:
        return render(request,"User/Post.html",{'postdata':post})

def DeletePost(request,did):
    tbl_post.objects.get(id=did).delete()
    return redirect("User:post")



def PageInsertSelect(request):
    pagedata=tbl_page.objects.filter(user=request.session["uid"])
    userID=tbl_user.objects.get(id=request.session["uid"])
    if request.method=="POST":
        tbl_page.objects.create(user=userID,page_name=request.POST.get("page_name"),page_bio=request.POST.get("page_bio"),page_photo=request.FILES.get("txtphoto")) 
        return redirect("User:PageInsertSelect")
    else:
        return render(request,"User/Page.html",{'pagedata':pagedata})

def Deletepage(request,did):
    tbl_page.objects.get(id=did).delete()
    return redirect("User:PageInsertSelect")



def viewrestaurant(request):
     district = tbl_district.objects.all()
     restaurants = tbl_restaurant.objects.all()
     return render(request,"User/viewrestaurant.html",{'dist': district, 'data':restaurants})
 
def ajaxrest(request):
     place = tbl_place.objects.get(id=request.GET.get("pid"))
     res= tbl_restaurant.objects.filter(place=place)
     return render(request,"User/AjaxRestaurant.html",{"res":res})


def viewfood(request,id):
     foodtype = tbl_foodtype.objects.all()
     category = tbl_category.objects.all()
     restaurants = tbl_restaurant.objects.get(id=id)
     request.session["restid"]=id
     food=tbl_food.objects.filter(rest=restaurants)
     return render(request,"User/Viewfood.html",{'type':foodtype,'food':food,'category':category})


def POSTComplaint(request):
    data=tbl_complaint.objects.filter(user=request.session["uid"])
    userID=tbl_user.objects.get(id=request.session["uid"])
    if request.method=="POST":
        title=request.POST.get('txttitle')
        details=request.POST.get('txtcomplaint')
        tbl_complaint.objects.create(complaint_title=title,complaint_details=details,user=userID)
        return redirect("User:POSTComplaint")
    else:
        return render(request,"User/POSTComplaint.html",{"data":data})
    
def delComplaint(request,did):
    tbl_complaint.objects.get(id=did).delete()
    return redirect("User:POSTComplaint")


def UserFeedback(request):
    data=tbl_feedback.objects.filter(user=request.session["uid"])
    userID=tbl_user.objects.get(id=request.session["uid"])
    if request.method=="POST":
        subject=request.POST.get('txtsubject')
        details=request.POST.get('txtfeedback')
        tbl_feedback.objects.create(feedback_subject=subject,feedback_details=details,user=userID)
        return redirect("User:UserFeedback")
    else:
        return render(request,"User/UserFeedback.html",{"data":data})
   

def delFeedback(request,did):
    tbl_feedback.objects.get(id=did).delete()
    return redirect("User:UserFeedback")

def ajaxFood(request):
    restaurants=tbl_restaurant.objects.get(id=request.session["restid"])
    if request.GET.get("fid")!="" and request.GET.get('cid')!="":
        type = tbl_foodtype.objects.get(id=request.GET.get('fid'))
        cat = tbl_category.objects.get(id=request.GET.get("cid"))
        food = tbl_food.objects.filter(foodtype=type,category=cat,rest=restaurants)
        return render(request,"User/AjaxFood.html",{'data':food}) 
    elif  request.GET.get("fid")=="" and request.GET.get('cid')!="":
       
        cat = tbl_category.objects.get(id=request.GET.get("cid"))
        food = tbl_food.objects.filter(category=cat,rest=restaurants)
        return render(request,"User/AjaxFood.html",{'data':food})
    elif  request.GET.get("fid")!="" and request.GET.get('cid')=="":
       
        type = tbl_foodtype.objects.get(id=request.GET.get('fid'))
        food = tbl_food.objects.filter(foodtype=type,rest=restaurants)
        return render(request,"User/AjaxFood.html",{'data':food})
    else:
        food = tbl_food.objects.filter(rest=restaurants)
        return render(request,"User/AjaxFood.html",{'data':food})
    
def addToCart(request,id):
    user=tbl_user.objects.get(id=request.session["uid"])
    food = tbl_food.objects.get(id=id)
    bookingcount=tbl_booking.objects.filter(user=user,booking_status=0).count()
    if bookingcount > 0:
        booking=tbl_booking.objects.get(user=user,booking_status=0)
        cartCount=tbl_cart.objects.filter(food=food,booking=booking).count()
        if cartCount > 0:
            return render(request,"User/ViewFood.html",{'msg':'Already in Cart','id':request.session["restid"]})
        else:
            tbl_cart.objects.create(
                food=food,booking=booking
            )
            return render(request,"User/ViewFood.html",{'msg':'Added to cart','id':request.session["restid"]})
    else:
        tbl_booking.objects.create(user=user,booking_status=0)
        booking=tbl_booking.objects.get(user=user,booking_status=0)
        cartCount=tbl_cart.objects.filter(food=food,booking=booking).count()
        if cartCount > 0:
            return render(request,"User/ViewFood.html",{'msg':'Already in Cart','id':request.session["restid"]})
        else:
            tbl_cart.objects.create(
                food=food,booking=booking
            )
            return render(request,"User/ViewFood.html",{'msg':'Added to cart','id':request.session["restid"]})
   
def Mycart(request):
   if request.method=="POST":
     bookingdata=tbl_booking.objects.get(id=request.session["bookingid"])
     bookingdata.booking_amount=request.POST.get("carttotalamt")
     bookingdata.booking_status=1
     bookingdata.save()
     return redirect("User:Pay")
   else:
    customerdata=tbl_user.objects.get(id=request.session["uid"])
    bcount=tbl_booking.objects.filter(user=customerdata,booking_status=0).count()
   #cartcount=cart.objects.filter(booking__customer=customerdata,booking__status=0).count()
    if bcount>0:
    #cartdata=cart.objects.filter(booking__customer=customerdata,booking__status=0)
     book=tbl_booking.objects.get(user=customerdata,booking_status=0)
     bid=book.id
     request.session["bookingid"]=bid
     bkid=tbl_booking.objects.get(id=bid)
     cartdata=tbl_cart.objects.filter(booking=bkid)
     return render(request,"User/MyCart.html",{'data':cartdata})
    else:
      return render(request,"User/MyCart.html")
def DelCart(request,did):
   tbl_cart.objects.get(id=did).delete()
   return redirect("User:mycart")
def CartQty(request):
   qty=request.GET.get('QTY')
   cartid=request.GET.get('ALT')
   cartdata=tbl_cart.objects.get(id=cartid)
   cartdata.cart_qty=qty
   cartdata.save()
   return redirect("User:mycart")

def Pay(request):
    bookingdata=tbl_booking.objects.get(id=request.session["bookingid"])
    amnt=bookingdata.booking_amount
    if request.method=="POST":
        bookingdata.booking_status=3
        bookingdata.save()
        return redirect("User:mycart")
    else:
        return render(request,"User/Payment.html",{'amnt':amnt})
    
def Viewbooking(request):
    customerdata=tbl_user.objects.get(id=request.session["uid"])
    booking=tbl_booking.objects.filter(user=customerdata,booking_status__gte=2)
    for cdata in booking:
        cartdata=tbl_cart.objects.filter(booking=cdata)
    return render(request,"User/ViewBooking.html",{'data':cartdata})




def ViewPost(request):
    userdata=tbl_user.objects.get(id=request.session["uid"])
    post=tbl_post.objects.all()
    return render(request,"User/ViewPost.html",{'postdata':post})

def Logout(request):
    del request.session['uid']
    return redirect('Guest:Login')
