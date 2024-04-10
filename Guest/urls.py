from django.urls import path
from Guest import views
app_name="Guest"
urlpatterns = [

    path('NewUser/',views.userRegistration,name="userRegistration"),
    path('NewResturant/',views.ResturantRegistration,name="ResturantRegistration"),
    path('NewDliveryBoy/',views.DliveryBoyRegistration,name="DliveryBoyRegistration"),
    
    path('Login/',views.Login,name="Login"),

    path('AjaxPlace/',views.ajaxplace,name="ajaxplace"),
    path('Index/',views.LoadMainIndex,name="LoadMainIndex"),
  
]