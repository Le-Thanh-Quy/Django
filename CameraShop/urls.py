from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:content>/search', views.search, name='search'),
    path('<int:id_camera>/camera', views.detail_camera, name='detail_camera'),
    path('<int:id_len>/len', views.detail_len, name='detail_len'),
]
