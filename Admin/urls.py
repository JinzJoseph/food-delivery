from django.urls import path
from Admin import views
app_name='Admin'

urlpatterns = [
    
      path('HomePage/',views.LoadingHomePage,name="LoadingHomePage"),
      
      path('AdminRegistration/', views.adminInsertSelect,name="adminInsertSelect"),
      path('delAdminReg/<int:did>', views.delAdminReg,name="delAdminReg"),
      path('adminRegUpdate/<int:eid>',views.adminRegUpdate,name="adminRegUpdate"),

     path('District/',views.District,name="District"), 
     path('del_district/<int:did>',views.DeleteDistrict,name="del_district"),
     path('edit_district/<int:eid>',views.EditDistrict,name="edit_district"),


     path('category/',views.Category,name="Category"),    
     path('del_category/<int:did>',views.DeleteCategory,name="del_category"),
     path('edit_category/<int:eid>',views.EditCategory,name="edit_category"),

    
     path('Complainttype/',views.Complainttype,name="Complainttype"),
     path('del_complainttype/<int:did>',views.DeleteComplainttype,name="del_complainttype"),
     path('edit_complainttype/<int:eid>',views.Editcomplainttype,name="edit_complainttype"),


     path('Place/',views.Place,name="Place"),
      path('del_place/<int:did>',views.DeletePlace,name="del_place"),

      path('Foodtype/',views.Foodtype,name="Foodtype"), 
     path('del_foodtype/<int:did>',views.DeleteFoodtype,name="del_foodtype"),
     path('edit_foodtype/<int:eid>',views.EditFoodtype,name="edit_foodtype"),


    path('UserListNew/',views.userListNew,name="userListNew"),
  

    path('ResturantListNew/',views.ResturantListNew,name="ResturantListNew"),
    path('acceptresturant/<int:aid>',views.acceptresturant,name="acceptresturant"),
    path('rejectresturant/<int:rid>',views.rejectresturant,name="rejectresturant"),
    path('ResturantListAccepted/',views.ResturantListAccepted,name="ResturantListAccepted"),
    path('ResturantListRejected/',views.ResturantListRejected,name="ResturantListRejected"),

    
    path('DeliveryBoyListNew/',views.DeliveryBoyListNew,name="DeliveryBoyListNew"),
    path('acceptdeliveryboy/<int:aid>',views.acceptdeliveryboy,name="acceptdeliveryboy"),
    path('rejectdeliveryboy/<int:rid>',views.rejectdeliveryboy,name="rejectdeliveryboy"),
    path('DeliveryBoyListAccepted/',views.DeliveryBoyListAccepted,name="DeliveryBoyListAccepted"),
    path('DeliveryBoyListRejected/',views.DeliveryBoyListRejected,name="DeliveryBoyListRejected"),

    path('ComplaintListNew/',views.ComplaintListNew,name="ComplaintListNew"),
    path('ComplaintReply/<int:cid>',views.ComplaintReply,name="ComplaintReply"),
    path('ComplaintSolved/',views.ComplaintSolved,name="ComplaintSolved"),


    path('UserFeedbackNew/',views.UserFeedbackNew,name="UserFeedbackNew"),
    path('logout/',views.logout,name="logout"),
    path('report/',views.viewbooking,name="report")


]