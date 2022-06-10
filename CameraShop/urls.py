from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:content>/search', views.search, name='search'),
]
