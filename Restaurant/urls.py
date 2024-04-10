from django.urls import path
from Restaurant import views
app_name='Restaurant'

urlpatterns = [
    
    


    path('home/',views.home,name="HomePage"),
    path('profile/',views.Myprofile,name="MyProfile"),
    path('editprofile/',views.Editprofile,name="EditProfile"),
    path('changepassword/',views.Changepassword,name="ChangePassword"),
    path('viewbooking/',views.viewbooking,name="viewbooking"),

    path('Food/',views.FoodInsertSelect,name="FoodInsertSelect"), 
    path('delFood/<int:did>',views.delFood,name="delFood"),

   
    path('viewproduct/<int:id>',views.viewproduct,name="viewproduct"),

    path('AssignNowDeliveryBoy/<int:did>',views.AssignNowDeliveryBoy,name="AssignNowDeliveryBoy"),
    path('logout/',views.Logout,name="logout")


    


]