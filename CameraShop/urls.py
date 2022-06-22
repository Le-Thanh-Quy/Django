from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('<str:content>/search', views.search, name='search'),
    path('<int:id_camera>/camera', views.detail_camera, name='detail_camera'),
    path('<int:id_len>/len', views.detail_len, name='detail_len'),
    path('<str:user_name>/profile', views.profile, name='profile'),
    path('<int:id_product>/<int:is_camera>/<int:is_buy>/add_cart', views.add_cart, name='add_cart'),
    path('<str:user_name>/order_page', views.order_page, name='order_page'),
    path('cast_payment/', views.cast_payment, name='cast_payment'),
    path('<int:bill_id>/bill_page', views.bill_page, name='bill_page'),
    path('<int:bill_id>/bill_cancel', views.bill_cancel, name='bill_cancel'),
]
