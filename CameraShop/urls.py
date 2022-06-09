from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('order_page/<int:user_id>', views.order_page),
]
