# pets/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_user, name='register_user'),
    path('login/', views.login_user, name='login_user'),
    path('add_pet/', views.add_pet, name='add_pet'),
    path('view_pets/', views.view_pets, name='view_pets'),
    path('adopt_pet/', views.adopt_pet, name='adopt_pet'),
    path('donate/', views.donate_to_fund, name='donate_to_fund'),
    path('view_balance/', views.view_fund_balance, name='view_fund_balance'),
]
