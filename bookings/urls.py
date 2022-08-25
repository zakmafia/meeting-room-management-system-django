from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:year>/<str:month>/', views.home, name = 'home'),
    path('add_rooms/', views.add_rooms, name='add_rooms'),
    path('add_available_times/', views.add_available_times, name='add_available_times'),
    path('create_booking/', views.create_booking, name='create_booking'),
    path('view_rooms/', views.view_rooms, name='view_rooms'),
]