from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_booking, name='create_booking'),
    # path('<int:year>/<str:month>/', views.home, name = 'home'),
    path('add_rooms/', views.add_rooms, name='add_rooms'),
    path('add_available_times/', views.add_available_times, name='add_available_times'),
    path('view_rooms/', views.view_rooms, name='view_rooms'),
    path('view_available_times/', views.view_available_times, name='view_available_times'),
    path('delete_room/<room_id>', views.delete_room, name='delete_room'),
    path('delete_time/<time_id>', views.delete_time, name='delete_time'),


    path('create_booking/', views.create_booking, name='create_booking'),

    path('cancel_booking_validate/<uidb64>/<token>/<booking_id>/', views.cancel_booking_validate, name='cancel_booking_validate'),
    path('cancel_booking_view/', views.cancel_booking_view, name="cancel_booking_view"),
    path('cancel_booking/<booking_id>/', views.cancel_booking, name='cancel_booking'),
    
]
