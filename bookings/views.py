from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from .models import Booking, Room, AvailableTime
from accounts.models import Account
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
    rooms = Room.objects.all()
    available_times = AvailableTime.objects.all()
    booking_time_am_pm = None

    if request.method == 'POST':
        name = request.POST['name']
        room = request.POST['room']
        booking_date = request.POST['date']
        booking_time = request.POST['time']
        description = request.POST['description']
        email = request.POST['email']

        splited_time = booking_time.split(" ")
        if splited_time[1].startswith("a"):
            booking_time_am_pm = splited_time[0] + " AM"
        else:
            booking_time_am_pm = splited_time[0] + " PM"
        print(booking_time_am_pm)

    

        parsed_time = datetime.strptime(booking_time_am_pm,"%I:%M %p").time()
        # # print(parsed_time)
        parsed_date = datetime.strptime(booking_date, "%Y-%d-%m").date()
        booking_time_instance = AvailableTime.objects.get(available_time__exact = parsed_time)
        room_instance = Room.objects.get(name__exact = room)
        
        try:
            if Account.objects.filter(email=email).exists():
                user = Account.objects.get(email__exact=email)
                booking = Booking.objects.create(
                    name = name,
                    booking_date = parsed_date,
                    booking_time = booking_time_instance,
                    room = room_instance,
                    description = description,
                    booking_person = user
                )
                booking.save()
                messages.success(request, 'Your have successfully booked a meeting room')
            else:
                messages.error(request, 'Register to use the booking system')
                return redirect('register')
        except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
            messages.error(request, 'Register to use the booking system')
            return redirect('register')
    context = {
        'rooms': rooms,
        'available_times': available_times,
        'current_year': current_year
        
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

def view_available_times(request):
    available_times = AvailableTime.objects.all()
    available_times_count = available_times.count()
    context = {
        'available_times': available_times,
        'available_times_count': available_times_count,
        'current_year': current_year
    }
    return render(request, 'bookings/view_available_times.html', context)

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

# def create_booking(request):
#     rooms = Room.objects.all()
#     available_times = AvailableTime.objects.all()
#     submitted = False
#     if request.method == "POST":
#         form = BookingForm(request.POST)
#         check_email = request.POST.get('booking_person')
#         # user = Account.objects.get(email__exact=check_email)
#         # print(user)
#         if form.is_valid():
#             # name = form.cleaned_data['name']
#             # booking_date = form.cleaned_data['booking_date']
#             # booking_time = form.cleaned_data['booking_time']
#             # room = form.cleaned_data['room']
#             # description = form.cleaned_data['description']
#             # checked_email = form.cleaned_data['booking_person']
#             # if Account.objects.filter(email=checked_email).exists():
#             #     user = Account.objects.get(email__exact=checked_email)
#             #     booking = Booking.objects.create(
#             #         name = name,
#             #         booking_date = booking_date,
#             #         booking_time = booking_time,
#             #         room = room,
#             #         description = description,
#             #         booking_person = user
#             #     )
#             # booking.save()
#             # print(checked_email)
#             form.save()
#             return HttpResponseRedirect('/create_booking?submitted=True')
#     else: 
#         form = BookingForm
#         if 'submitted' in request.GET:
#             submitted = True
#     context = {
#         'form': form,
#         'rooms': rooms,
#         'available_times': available_times,
#         'submitted': submitted
#     }
#     return render(request, 'bookings/bookings.html', context)