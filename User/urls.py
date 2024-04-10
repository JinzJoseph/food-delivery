from django.urls import path,include
from User import views
app_name='User'

urlpatterns = [
    path('Userhome/',views.user_home,name="Userhome"),


    path('Myprofile/',views.Myprofile,name="Myprofile"),
    path('Editprofile/',views.Editprofile,name="Editprofile"),


    path('changepassword/',views.changepassword,name="changepassword"),
    
 

    path('Post/',views.Post,name="Post"),
    path('del_post/<int:did>',views.DeletePost,name="del_post"),
    path('ViewPost/',views.ViewPost,name="ViewPostiewPost"),

    path('Page/',views.PageInsertSelect,name="PageInsertSelect"),
    path('del_page/<int:did>',views.Deletepage,name="del_page"),
    
    
    path('SearchRestaurant/',views.viewrestaurant,name="SearchRestaurant"),
    path('ajaxrest/',views.ajaxrest,name="ajaxrest"),
    path('viewfood/<int:id>',views.viewfood,name="viewfood"),
    path('ajaxfood/',views.ajaxFood,name="ajaxfood"),
    path('addCart/<int:id>',views.addToCart,name="addCart"),
    path('Mycart/', views.Mycart, name='mycart'),
    path('DelCart/<int:did>', views.DelCart, name='delcart'),
    path('CartQty/', views.CartQty, name='cartqty'),
    path('Pay/', views.Pay, name='Pay'),
    path('Viewbooking/', views.Viewbooking, name='Viewbooking'),
    
    path('POSTComplaint/',views.POSTComplaint,name="POSTComplaint"),
    path('delComplaint/<int:did>',views.delComplaint,name="delComplaint"),

    path('UserFeedback/', views.UserFeedback, name='UserFeedback'),
    path('delFeedback/<int:did>',views.delFeedback,name="delFeedback"),
    path('logout',views.Logout,name="Logout")

]