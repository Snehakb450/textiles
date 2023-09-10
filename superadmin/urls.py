from django.urls import path
from . import views
app_name='superadmin'

urlpatterns = [
    path ('admin_master/',views.get_admin_master, name="admin_master"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('add_seller/',views.add_seller,name="add_seller"),
    path('admin_change/',views.admin_change,name="admin_change"),
    path('logout/',views.logout,name="logout"), 
     path('admin_login/',views.admin_login,name="admin_login"),
     path('deleteseller/<int:a_id>',views.deleteseller, name="deleteseller"), 
     path('update_seller_status/', views.update_seller_status, name='update_seller_status'),
    path('forgot/',views.forgot,name="forgot"),
    path('',views.home,name="home") 
]