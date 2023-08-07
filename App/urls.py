from django.contrib import admin
from django.urls import path
from . import views
from .models import MyDb

app_name = 'MyDb'

urlpatterns =[
    path('', views.HomePage),
    path('a/', views.AboutPage),
    path('c/', views.Conta ctPage),
    path('s/', views.ServicesPage),
    path('i/', views.index),
    path('adp/', views.Admin),
    path('delete/<int:UserId>/',views.delete,name='delete'),
    path('update/<int:UserId>/',views.update,name='update'),
]