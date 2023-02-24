from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('accounts/login/', views.login_view, name='login_view'),
    path('accounts/logout/', views.LogoutView.as_view(), name='logout'),
    path('accounts/register/', views.register, name='register'),
    path('admin/', views.admin, name='adminpage'),
]