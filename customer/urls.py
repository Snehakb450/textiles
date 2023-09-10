from django.urls import path
from . import views
app_name='customer'

urlpatterns = [
    path ('customer_home/',views.get_customer_home, name="customer_home"),
    path ('signup/',views.signup, name="signup"),
    path ('verify_otp/',views.verify_otp, name="verify_otp"), 
    path('login/',views.login,name="login"),
    path ('customer_master/',views.get_customer_master, name="customer_master"),
    path ('customer_profile/',views.customer_profile, name="customer_profile"),
    path ('view_cart/',views.view_cart, name="view_cart"),
    path ('change/',views.change, name="change"),
    path ('logout/',views.logout, name="logout"),
    path ('edit_profile/<int:c_id>',views.edit_profile, name="edit_profile"),
    path('search_product/',views.search_product,name="search_product"),
    path('view_product/<int:id>',views.view_product,name="view_product") ,
    path('addtobag/', views.add_to_bag, name="addtobag"),
    path('remove/<int:p_id>',views.remove,name="remove") ,
    path('forgot/',views.forgot,name="forgot") 
]