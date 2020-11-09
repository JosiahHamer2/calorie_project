from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_view
from .views import *
from . import views

urlpatterns = [
	#path('signup/', SignUpView.as_view(), name='signup'),
	path('', views.home, name = 'home'),
	path('user/', views.userPage, name = 'userPage'),
	path('product/', views.Fooditem, name = 'fooditem'),
	path('createfooditem/', views.createfooditem, name = 'createfooditem'),
	path('addFooditem/', views.addFooditem, name = 'addFooditem'),
]