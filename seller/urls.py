from django.urls import path
from . import views
app_name='seller'

urlpatterns = [
    path('seller_login/',views.seller_login,name="seller_login"),
    path('seller_signup/',views.seller_signup,name="seller_signup"),
    path('seller_master/',views.seller_master,name="seller_master"),
    path('seller_add/',views.seller_add,name="seller_add"),
    path('seller_product/',views.seller_product,name="seller_product"),
    path('seller_change/',views.seller_change,name="seller_change"),
    path('logout/',views.logout,name="logout"),
    path('edit_product/<int:s_id>',views.edit_product,name="edit_product"),
    path('delete_product/<int:s_id>',views.delete_product,name="delete_product"), 
    path('forgot/',views.forgot,name="forgot") 
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)