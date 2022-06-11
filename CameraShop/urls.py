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

]
