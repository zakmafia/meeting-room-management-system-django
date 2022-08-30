from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:year>/<str:month>/', views.home, name = 'home'),
    path('add_rooms/', views.add_rooms, name='add_rooms'),
    path('add_available_times/', views.add_available_times, name='add_available_times'),
    path('create_booking/', views.create_booking, name='create_booking'),
    path('view_rooms/', views.view_rooms, name='view_rooms'),
    path('view_available_times/', views.view_available_times, name='view_available_times'),

    path('cancel_booking_validate/<uidb64>/<token>/', views.cancel_booking_validate, name='cancel_booking_validate'),
    path('cancel_booking_view', views.cancel_booking_view, name="cancel_booking_view"),
    
]
