from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.http import HttpResponseRedirect, HttpResponse
from .models import Booking, Room
from .forms import BookingForm, RoomForm, AvailableTimeForm
# Create your views here.
now = datetime.now()
current_year = now.year

def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    name = 'Zekarias'
    month = month.capitalize()
    month_number = int(list(calendar.month_name).index(month))
    cal = HTMLCalendar().formatmonth(year, month_number)
    time = now.strftime('%I:%M %p')
    context = {
        'name': name,
        'year': year,
        'month': month,
        'month_number': month_number,
        'cal':cal,
        'current_year': current_year,
        'time': time,
    }
    return render(request, 'home.html', context)

def add_rooms(request):
    submitted = False
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_rooms?submitted=True')
    else: 
        form = RoomForm
        if 'submitted' in request.GET:
            submitted = True
    context = {
        'form': form,
        'submitted': submitted,
        'current_year': current_year
    }
    return render(request, 'bookings/add_rooms.html', context)

def add_available_times(request):
    submitted = False
    if request.method == "POST":
        form = AvailableTimeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_available_times?submitted=True')
    else: 
        form = AvailableTimeForm
        if 'submitted' in request.GET:
            submitted = True
    context = {
        'form': form,
        'submitted': submitted,
        'current_year': current_year
    }
    return render(request, 'bookings/add_available_times.html', context)

def create_booking(request):
    submitted = False
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/create_booking?submitted=True')
    else: 
        form = BookingForm
        if 'submitted' in request.GET:
            submitted = True
    context = {
        'form': form,
        'submitted': submitted
    }
    return render(request, 'bookings/bookings.html', context)

def view_rooms(request):
    rooms = Room.objects.all()
    rooms_count = rooms.count()
    context = {
        'rooms': rooms,
        'current_year': current_year,  
        'rooms_count': rooms_count,  
    }
    return render(request, 'bookings/view_rooms.html', context)

def room_detail(request):
    return render(request, 'bookings/room_detail.html')

# def all_bookings(request):
#     booking_list = Booking.objects.all()
#     context = {
#         'booking_list': booking_list
#     }
#     return render(request, 'bookings/booking_list.html', context)

# def display_rooms(request):
#     rooms = Room.objects.all()
#     context = {
#         'rooms': rooms,
#     }
#     return render(request, 'home.html', context)
