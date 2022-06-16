from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('order_page/<int:user_id>', views.order_page),
    path('bill_page/<int:user_id>', views.bill_page),
    path('history_page/<int:user_id>', views.history_page),
]
