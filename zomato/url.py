# zomato/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.display_menu, name='menu'),
     path('updatemenu/', views.update_menu, name='menu'),
      path('create/', views.addnew, name='menu'),
       path('delete/', views.deletone, name='menu'),
]
