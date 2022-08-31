from dataclasses import field
from tkinter.tix import Select
from django import forms
from django.forms import ModelForm
from .models import Booking, Room, AvailableTime
from accounts.models import Account

# choices = Account.objects.all().values_list('email', 'email')
# choices_list = []
# for item in choices:
#     choices_list.append(item)

# print(choices_list)

# Create a booking Form
class DateInput(forms.DateInput):
    input_type = 'date'


class BookingForm(ModelForm):
    booking_date = forms.DateField(widget=DateInput)
    # booking_person = forms.EmailField()
    class Meta:
        model = Booking
        fields = ('name', 'booking_date', 'booking_time', 'room', 'description', 'booking_person')
        labels = {
            'name': '',
            'booking_date': '',
            'booking_time': '',
            'room': '',
            'description': '',
            'booking_person': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the booking name'}),
            'booking_date': forms.TextInput(attrs={'class': 'form-control','name':'date', 'id':'date'},),
            'booking_time': forms.Select(attrs={'class': 'form-control'}),
            'room': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter the description'}),
            'booking_person': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
        }
    
    # def clean(self):
    #     cleaned_data = super(BookingForm, self).clean()
    #     # booking_date = cleaned_data.get('booking_date')
    #     booking_person = cleaned_data.get('booking_person')
    #     print(booking_person)
    #     if Account.objects.filter(email=booking_person).exists():
    #         user = Account.objects.get(email__exact=booking_person)
    #         booking_person = user
    #     else:
    #         raise forms.ValidationError(
    #             "This user is not registered!"
    #         )



class RoomForm(ModelForm):
    images = forms.ImageField()
    class Meta:
        model = Room
        fields = ['name', 'address', 'images']

    def __init__(self, *args, **kwargs):
        super(RoomForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Enter the room name'
        self.fields['address'].widget.attrs['placeholder'] = 'Enter the room address'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

class AvailableTimeForm(ModelForm):
    class Meta:
        model = AvailableTime
        fields = ('available_time',)
        labels ={
            'available_time': ''
        }
        widgets = {
            'available_time': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the available times'})
        }
