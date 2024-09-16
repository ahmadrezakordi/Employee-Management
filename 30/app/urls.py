from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('login-redirect/', login_redirect, name='login-redirect'),
    path('register/', RegisterView.as_view(), name='register'),
    path('add-item/', AddEmployee.as_view(), name='add-item'),
    path('edit-item/<int:pk>', EditEmployee.as_view(), name='edit-item'),
    path('delete-item/<int:pk>', DeleteEmployee.as_view(), name='delete-item'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
]
