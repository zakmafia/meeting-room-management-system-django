from django.contrib import admin
from .models import Room, Booking, AvailableTime
# Register your models here.

# admin.site.register(Room)
# admin.site.register(Booking)
# admin.site.register(AvailableTime)


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name','slug','address')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('name',)
    search_fields = ('name', 'address')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    fields = ('name', 'room', 'booking_date','booking_time','description', 'booking_person')
    list_display = ('name', 'booking_date', 'room')
    list_filter = ('room', 'booking_date')
    ordering = ('booking_date',)
    search_fields = ('name', 'room')

@admin.register(AvailableTime)
class AvailableTimeAdmin(admin.ModelAdmin):
    list_display = ('available_time',)