from django.contrib import admin
from django.urls import path, include
from . import views
from .views import CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.create, name='home'),
    path('delete/<str:pk>/', views.delete, name='delete'),
    path('update/<str:pk>/', views.update, name='update'),
    path('login', CustomLoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
    path('register', RegisterPage.as_view(), name='register')
]