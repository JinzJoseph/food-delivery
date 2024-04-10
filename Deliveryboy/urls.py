from django.urls import path
from Deliveryboy import views
app_name='Deliveryboy'

urlpatterns = [



    path('home/',views.HomePage,name="HomePage"),
     path('profile/',views.Myprofile,name="MyProfile"),
     path('editprofile/',views.Editprofile,name="Editprofile"),
     path('changepassword/',views.Changepassword,name="ChangePassword"),

    path('AssignedOrder/',views.AssignedOrder,name="AssignedOrder"),
    path('logout/',views.Logout,name="logout")


]